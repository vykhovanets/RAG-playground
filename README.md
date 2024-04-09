# RAG-playground

## Iteration #1

_The goal of the first iteration is to have local application which will make API calls to LLM providers_

Currently supports Ollama's Mistral and OpenAI, uses Chroma as a vector storage. Implemented basic RAG capabilities.

## Instructions

### Setup

1. clone repository

```bash
https://github.com/vykhovanets/RAG-playground.git && cd RAG-playground
```

2. add `.env` file into `RAG-playground` folder with the following content:

```
# API keys
OPENAI_API_KEY=...
# COHERE_API_KEY=...
# ANTHROPIC_API_KEY=...
# HF_API_KEY=...

# Persistence
PROJECTS_DIR='./data/projects'
HISTORIES_DIR='./data/histories'
DB='./data/db'
```

3. install dependencies

```bash
python3.12 -m venv .envs/py-12 && source .envs/py-12/bin/activate
pip install uv && uv pip install -r requirements.txt
```

4. run app from the virtual environment

```bash
source .envs/py-12/bin/activate
streamlit run playground/main.py
```

### Documents

- [Stages of RAG](docs/00-stages-of-rag.md)
- [Web app with Streamlit](docs/01-streamlit.md)
- [Chroma retrieval](docs/02-choma-parctises.md)
- [Python stuff](docs/03-python-stuff.md)
