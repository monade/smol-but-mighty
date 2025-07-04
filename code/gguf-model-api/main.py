import os
from dotenv import load_dotenv
from llama_cpp import Llama
import json
import re
from typing import List, Dict, Any, Optional
from textwrap import dedent
from transformers import AutoTokenizer
from huggingface_hub import hf_hub_download, snapshot_download
from pydantic import BaseModel

huggingface_hub_path = "monadestudio/smol-function-calling-gguf"

model_path = snapshot_download(
    repo_id=huggingface_hub_path,
    local_dir="./models"
)

# # Get absolute path to workspace
# WORKSPACE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# # Set up environment variables
# os.environ["TRANSFORMERS_CACHE"] = os.path.join(WORKSPACE_DIR, "peft-lora-finetune/cache")
# os.environ["HF_HOME"] = os.environ["TRANSFORMERS_CACHE"]
# os.makedirs(os.environ["TRANSFORMERS_CACHE"], exist_ok=True)

load_dotenv()

def get_chat_interaction(prompt: str, functions: list[dict]) -> List[Dict[str, str]]:
    """Create a chat interaction with the given prompt."""
    return [
        {
            "role": "system",
            "content": dedent("""
You are a helpful assistant with access to the following functions. Use them if required -
{functions}
""").format(functions=json.dumps(functions))
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

def format_prompt(chat_interaction: List[Dict[str, str]]) -> str:
    """Format the chat interaction into a prompt string."""
    tokenizer = AutoTokenizer.from_pretrained(
        huggingface_hub_path, padding=True, truncation=True, max_length=512
    )
    formatted_prompt = tokenizer.apply_chat_template(chat_interaction, tokenize=False)

    return formatted_prompt

# Helper function to clean json function calls
def extract_fncall(resp):
    resp_funcs_iters = list(re.finditer('functioncall>', resp))[:2]
    if len(resp_funcs_iters): 
        resp = resp[resp_funcs_iters[0].end():].strip()
        if len(resp_funcs_iters)>1:
            resp_funcs_iter = next(re.finditer('functioncall>', resp))
            resp = resp[:resp_funcs_iter.start()-1].strip()
            if resp.endswith('/'):
                resp = resp[:-1]
        try:
            resp = json.dumps(json.loads(resp))
        except json.JSONDecodeError:
            pass
    return resp

def load_gguf_model(model_path: str) -> Llama:
    """Load the GGUF model."""
    # Convert to absolute path
    model_path = os.path.abspath(model_path)
    if not os.path.exists(model_path):
        raise ValueError(f"Model path does not exist: {model_path}")
    
    print(f"Loading GGUF model from: {model_path}")
    return Llama(
        model_path=model_path,
        n_ctx=512,  # Match the training context length
        n_batch=512,
        n_threads=4,  # Adjust based on your CPU
        n_gpu_layers=0  # Set to -1 for all layers on GPU, 0 for CPU only
    )

def generate_text(model: Llama, prompt: str, max_tokens: int = 128) -> str:
    """Generate text using the GGUF model."""
    # Generate response
    response = model(
        prompt,
        max_tokens=max_tokens,
        temperature=0.7,
        top_p=0.95,
        stop=["</s>", "<|user|>", "<|system|>", "<|im_end|>"],  # Stop at these tokens
        echo=False  # Don't include the prompt in the output
    )
    
    # Extract the generated text
    generated_text = response["choices"][0]["text"]
    
    # Clean up the response
    generated_text = generated_text.strip()
    
    return generated_text

# Load the model
model = load_gguf_model(f"{model_path}/model-auto.gguf")

from fastapi import FastAPI
from typing import Union
import json

class CallBody(BaseModel):
    prompt: str
    functions: list[dict]

app = FastAPI()

@app.post("/call")
def call_function(body: CallBody = CallBody(
    prompt="What is the weather in Rome?",
    functions=[
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The location to get the weather for"}
                }
            }
        },
        {
            "name": "get_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "The location to get the weather for"}
                }
            }
        }
    ]
)):
    """Calls a function passing the correct arguments from a given user prompt and a list of available functions."""
    chat = get_chat_interaction(body.prompt, body.functions)
    formatted_prompt = format_prompt(chat)

    # Generate response
    response = generate_text(model, formatted_prompt)
    
    # Extract function call if present
    fn_call = extract_fncall(response)
    
    return { "response": json.loads(fn_call) }