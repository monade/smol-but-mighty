# Smol but Mighty

Questo progetto nasce come workshop per la [Working Software 2025](https://www.agilemovement.it/workingsoftware/) a Reggio Emilia.

In questa repository si mostrano due esempi di fine-tuning di Small Language Models (SLM) usando SFT e LoRA.

Inoltre si mostra come preparare un modello per la distribuzione in GGUF e come servirne il servizio con FastAPI.

## Introduzione
Questo workshop è pensato per chi ha già familiarità con l'utilizzo di Python, conosce per sommi capi la teoria di base dietro al machine learning, ma non ha mai addestrato un modello.


## Prerequisiti

Partiremo dal modello [SmolLM 2](https://huggingface.co/monade/SmolLM-2-135M-Instruct) di 135M parametri creato da Hugging Face.

Tutti gli esempi (tranne l'ultimo, di cui è fornito il codice completo) sono eseguiti in Google Colab, dove non è necessario installare nulla.

Se preferisci eseguire i notebook localmente, puoi usare clonare questa repository e  seguire [questa guida](https://jupyter-docker-stacks.readthedocs.io/en/latest/) per avviare l'ambiente Jupyter su Docker. È necessario Docker e una GPU compatibile con CUDA.


## Esempi previsti
| Nome | Descrizione | Colab |
|---|---|---|
| Sentiment Classification | Finetuning SFT per classificare il __sentiment__ di recensioni Amazon | [Colab](https://colab.research.google.com/github/monade/smol-but-mighty/blob/main/notebooks/01_sentiment_classification.ipynb) |
| Function Calling | Finetuning con LoRA per addestrare un modello a invocare funzioni a partire da una richiesta testuale | [Colab](https://colab.research.google.com/github/monade/smol-but-mighty/blob/main/notebooks/02_function_calling.ipynb) |
| GGUF Conversion | Conversione in GGUF di un modello già addestrato | [Colab](https://colab.research.google.com/github/monade/smol-but-mighty/blob/main/notebooks/03_gguf_conversion.ipynb) |
| GGUF Serving | Un esempio su come servire un modello GGUF con FastAPI | [Colab](https://colab.research.google.com/github/monade/smol-but-mighty/blob/main/notebooks/04_gguf_serving.ipynb) |


## Credits

Questo corso nasce come iniziativa di formazione di [Monade](https://monade.io).

- [@monade](https://github.com/monade)
- [@ProGM](https://github.com/ProGM)
- [@nick990](https://github.com/nick990)
- [@lcastelnovo](https://github.com/lcastelnovo)

Il corso è ispirato dal corso [Smol Course](https://github.com/huggingface/smol-course) di [@huggingface](https://github.com/huggingface).
