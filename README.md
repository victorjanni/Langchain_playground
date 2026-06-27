# LangChain Playground 🚀

Welcome to the **LangChain Playground**, a comprehensive hands-on repository designed to learn, experiment, and build with the [LangChain](https://github.com/langchain-ai/langchain) ecosystem. This repository covers everything from the absolute basics of LLMs and Chat Models to advanced concepts like Retrieval-Augmented Generation (RAG), Memory, LangChain Expression Language (LCEL), LangServe, and custom Agents.

---

## 📂 Repository Structure

The repository is organized into distinct directories representing different stages of learning and project development:

### 1. [Basics of LangChain](file:///e:/Langchain_playground/Basics_of_Langchain)
This folder contains step-by-step guides and Jupyter Notebooks covering core LangChain concepts:
*   **[1.1-openai](file:///e:/Langchain_playground/Basics_of_Langchain/1.1-openai)**: Getting started with the OpenAI API integration and building a basic application.
*   **[1.LLMs](file:///e:/Langchain_playground/Basics_of_Langchain/1.LLMs)**: Demos illustrating standard LLM (Large Language Model) interfaces.
*   **[2.chatModels](file:///e:/Langchain_playground/Basics_of_Langchain/2.chatModels)**: Examples of using Chat Models from various providers, including:
    *   OpenAI (`1_openai_chatmodel.py`)
    *   Anthropic (`2_anthropic_chatmodel.py`)
    *   Google Gemini (`3_gemini_chatmodel.py`)
    *   HuggingFace API (`4_hf_chatmodel_api.py`)
    *   HuggingFace Local (`5_hf_local_chatmodel.py`)
*   **[3.2-DataIngestion](file:///e:/Langchain_playground/Basics_of_Langchain/3.2-DataIngestion)**: Techniques and tools for reading, loading, and parsing external source data into LangChain documents.
*   **[3.3-Data Transformer](file:///e:/Langchain_playground/Basics_of_Langchain/3.3-Data%20Transformer)**: Text splitting strategies to prepare documents for embedding:
    *   `CharacterTextSplitter`
    *   `RecursiveCharacterTextSplitter`
    *   `HTMLTextSplitter`
    *   `RecursiveJsonSplitter`
*   **[4-Embeddings](file:///e:/Langchain_playground/Basics_of_Langchain/4-Embeddings)**: Generating dense vector representations using OpenAI, Hugging Face (local/remote), and Ollama.
*   **[5-VectorStore](file:///e:/Langchain_playground/Basics_of_Langchain/5-VectorStore)**: Storing and querying vector embeddings using:
    *   **FAISS** (Facebook AI Similarity Search)
    *   **ChromaDB**
*   **[6-memory](file:///e:/Langchain_playground/Basics_of_Langchain/6-memory)**: Implementing conversational memory state in LLM applications and chatbots.
*   **[serve.py](file:///e:/Langchain_playground/Basics_of_Langchain/serve.py)**: A FastAPI & LangServe backend application that serves a translation chain at the `/chain` endpoint using Groq (`llama-3.1-8b-instant`).
*   **[simplellmLCEL.ipynb](file:///e:/Langchain_playground/Basics_of_Langchain/simplellmLCEL.ipynb)**: Introduction to LangChain Expression Language (LCEL) syntax and chain pipelining.

### 2. [Latest LangChain Features](file:///e:/Langchain_playground/latestlangchain)
Notebooks covering newer features, tool execution, and agents:
*   **[1-langchain-intro.ipynb](file:///e:/Langchain_playground/latestlangchain/1-langchain-intro.ipynb)**: Introductory walkthrough to the current LangChain API.
*   **[2-modelintegration.ipynb](file:///e:/Langchain_playground/latestlangchain/2-modelintegration.ipynb)**: Integration setups for modern frontier models.
*   **[3-tools.ipynb](file:///e:/Langchain_playground/latestlangchain/3-tools.ipynb)**: Defining and registering custom tools for LLMs.
*   **[4-tool-calling-in-langchain.ipynb](file:///e:/Langchain_playground/latestlangchain/4-tool-calling-in-langchain.ipynb)**: Orchestrating structured tool calls with LLMs.
*   **[5-agents-in-langchain.ipynb](file:///e:/Langchain_playground/latestlangchain/5-agents-in-langchain.ipynb)**: Building autonomous agents with tools.

### 3. [LangChain Basic Projects](file:///e:/Langchain_playground/Langchain_basic_projects)
End-to-end applications demonstrating practical use cases:
*   **[basic_rag_project.ipynb](file:///e:/Langchain_playground/Langchain_basic_projects/basic_rag_project.ipynb)**: A complete Retrieval-Augmented Generation (RAG) system matching user queries against ingested documents.
*   **[simpleLCELllm.ipynb](file:///e:/Langchain_playground/Langchain_basic_projects/simpleLCELllm.ipynb)**: Building sequential chains using LCEL.

---

## 🛠️ Setup & Installation

This project utilizes `uv` as its fast Python package and project manager. Follow the steps below to set up your environment:

### Prerequisites
Make sure you have [uv](https://github.com/astral-sh/uv) installed. If you don't, you can install it via:
```bash
pip install uv
```

### Installation
1.  **Clone the repository** (or open the project directory).
2.  **Sync the environment & install dependencies**:
    ```bash
    uv sync
    ```
    This will automatically create a virtual environment and install all dependencies defined in `pyproject.toml`.

3.  **Activate the virtual environment**:
    *   **Windows (PowerShell)**:
        ```powershell
        .venv\Scripts\Activate.ps1
        ```
    *   **macOS / Linux**:
        ```bash
        source .venv/bin/activate
        ```

---

## 🔑 Environment Configuration

Create a `.env` file in the root of the project (if not already present) and add your API keys. Refer to the variables below:

```env
# LLM Providers API Keys
OPENAI_API_KEY="your-openai-api-key"
GOOGLE_API_KEY="your-google-gemini-api-key"
GROQ_API_KEY="your-groq-api-key"
ANTHROPIC_API_KEY="your-anthropic-api-key"
HUGGINGFACEHUB_API_TOKEN="your-huggingface-token"

# LangSmith Tracing & Monitoring (Optional)
LANGSMITH_API_KEY="your-langsmith-api-key"
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_PROJECT="langchain-playground"
```

---

## 🚀 Running the Applications

### 1. Interactive Notebooks
You can run any of the Jupyter notebooks (`.ipynb`) in your editor (VS Code, Cursor, Jupyter Lab, etc.). Make sure to select the `.venv` virtual environment as your Jupyter kernel.

### 2. Run Python Scripts
Run individual python files from the command line:
```bash
uv run python Basics_of_Langchain/2.chatModels/1_openai_chatmodel.py
```

### 3. Start the LangServe Server
Serve the FastAPI/LangServe translation service locally:
```bash
uv run python Basics_of_Langchain/serve.py
```
Once started, the API will be available at `http://localhost:8000`. You can test it using the interactive playground at `http://localhost:8000/chain/playground/`.

---

## 🧰 Dependencies & Tools

Key libraries configured in this environment (see [pyproject.toml](file:///e:/Langchain_playground/pyproject.toml) for versions):
*   **LangChain core components**: `langchain`, `langchain-core`, `langchain-community`, `langchain-experimental`
*   **Model providers**: `langchain-openai`, `langchain-anthropic`, `langchain-google-genai`, `langchain-groq`, `langchain-huggingface`, `langchain-ollama`
*   **Vector Databases**: `chromadb`, `faiss-cpu`, `langchain-chroma`
*   **Web Frameworks / Deployment**: `fastapi`, `uvicorn`, `langserve`, `sse-starlette`, `streamlit`
*   **Data Parsing / Utilities**: `pypdf`, `pymupdf`, `beautifulsoup4`, `wikipedia`, `arxiv`, `python-dotenv`
