# GGUF serving con FastAPI

## Descrizione

Questo progetto è un esempio di come servire un modello GGUF con FastAPI.

Il modello è un modello di funzione chiamata addestrato su un dataset di esempi di prompt e funzioni.

Il modello è [disponibile su Hugging Face](https://huggingface.co/monadestudio/smol-function-calling-gguf) ed è stato addestrato nel notebook [03_gguf_conversion.ipynb](../../notebooks/03_gguf_conversion.ipynb).

## Setup

Installare le dipendenze usando [Poetry](https://python-poetry.org/):

```bash
poetry install
```

## Avviare il server

Avviare il server con FastAPI:

```bash
poetry run fastapi dev main.py
```

Ora puoi aprire http://localhost:8000/docs per vedere la documentazione dell'API.
