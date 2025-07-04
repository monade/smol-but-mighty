# Smol but Mighty: Fine-tuning di Small Language Models

Questo progetto nasce come workshop per la [Working Software 2025](https://www.agilemovement.it/workingsoftware/) a Reggio Emilia.

In questa repository si mostrano due esempi di fine-tuning di Small Language Models (SLM) usando SFT e LoRA.

Inoltre si mostra come preparare un modello per la distribuzione in GGUF e come esporlo come API con FastAPI.

## Introduzione
Questo workshop è pensato per chi ha già familiarità con l'utilizzo di Python, conosce per sommi capi la teoria di base dietro al machine learning (Neural Networks e Backpropagation), ma non ha mai addestrato un modello.

Per iniziare, trovi le slide e l'introduzione testuale presentata durante il workshop nella cartella [docs](./tree/main/docs).

## Prerequisiti

Partiremo dal modello [SmolLM2](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct) da 135M parametri creato da Hugging Face.

Tutti gli esempi (tranne l'ultimo, pensato per essere eseguito localmente) sono progettati per funzionare su Google Colab, senza necessità di installare nulla.

Se preferisci eseguire i notebook localmente, puoi clonare questa repository e  seguire [questa guida](https://jupyter-docker-stacks.readthedocs.io/en/latest/) per avviare l'ambiente Jupyter su Docker. Per l'esecuzione locale è necessario avere Docker installato e disporre di una GPU compatibile con CUDA.


## Esempi previsti
| Nome | Descrizione | Link |
|---|---|---|
| Sentiment Classification | Finetuning SFT per classificare il __sentiment__ di recensioni Amazon | [Colab](https://colab.research.google.com/github/monade/smol-but-mighty/blob/main/notebooks/01_sentiment_classification.ipynb) |
| Function Calling | Finetuning con LoRA per addestrare un modello a invocare funzioni a partire da una richiesta testuale | [Colab](https://colab.research.google.com/github/monade/smol-but-mighty/blob/main/notebooks/02_function_calling.ipynb) |
| GGUF Conversion | Conversione in GGUF di un modello già addestrato | [Colab](https://colab.research.google.com/github/monade/smol-but-mighty/blob/main/notebooks/03_gguf_conversion.ipynb) |
| GGUF Serving | Un esempio su come servire un modello GGUF con FastAPI | [Progetto](./tree/main/code/gguf-model-api) |


## Credits

Questo corso nasce come iniziativa di formazione di [Mònade](https://monade.io).

Partecipanti:
- [@ProGM](https://github.com/ProGM)
- [@nick990](https://github.com/nick990)
- [@lcastelnovo](https://github.com/lcastelnovo)
- [@caiodark](https://github.com/caiodark)

Il corso è ispirato dal corso [Smol Course](https://github.com/huggingface/smol-course) di [@huggingface](https://github.com/huggingface).
