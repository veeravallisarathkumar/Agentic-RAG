# 🤖 Agentic RAG — Intelligent Document Q&A with Autonomous Agents

> A production-ready **Agentic Retrieval-Augmented Generation (RAG)** system that combines autonomous AI agents with vector-based document retrieval, delivered through an interactive Streamlit web interface.

-----

## 🎯 What This Project Does

Traditional RAG systems retrieve documents and generate a response — and stop there. **Agentic RAG goes further**: it uses autonomous AI agents that can **reason, plan, and iteratively retrieve** information to answer complex, multi-step questions with greater accuracy.

This project implements an end-to-end pipeline where:

- Documents are ingested, chunked, and stored as vector embeddings
- An AI agent decides *when* and *what* to retrieve based on the question
- The agent reasons over the retrieved context and produces a grounded answer
- Everything is accessible via a clean, interactive **Streamlit UI**

-----

## ✨ Key Features

- **Agentic Reasoning** — The system uses an LLM-powered agent that autonomously decides retrieval strategies rather than relying on a fixed pipeline
- **Vector Search** — Efficient semantic search over documents using embeddings
- **Streamlit Interface** — User-friendly chat interface for real-time Q&A
- **Modular Codebase** — Clean separation of concerns with `src/` for core logic and `main.py` as the entry point
- **Environment Configuration** — Secure API key management via `.env`
- **Reproducible Setup** — Dependency management via `requirements.txt` and `pyproject.toml`

-----

## 🏗️ Project Architecture

```
Agentic-RAG/
│
├── main.py               # Core RAG pipeline & agent logic
├── streamlit_app.py      # Streamlit frontend (chat UI)
│
├── src/                  # Source modules
│   ├── agent/            # Agent definitions and tool setup
│   ├── retriever/        # Vector store & retrieval logic
│   └── utils/            # Helper functions
│
├── data/                 # Input documents for ingestion
│
├── .env                  # API keys (not committed)
├── requirements.txt      # Python dependencies
└── pyproject.toml        # Project configuration
```

-----

## 🧠 How Agentic RAG Works

```
User Question
     │
     ▼
 AI Agent  ──► Decides retrieval strategy
     │
     ▼
Vector Store ──► Retrieves relevant document chunks
     │
     ▼
 LLM Reasoning ──► Synthesizes answer from context
     │
     ▼
 Final Answer (grounded in your documents)
```

Unlike native RAG, the agent can:

- Re-query with refined search terms if the first retrieval is insufficient
- Combine information from multiple chunks
- Know when it has enough context to answer confidently

-----

## 🛠️ Tech Stack

|Layer          |Technology               |
|---------------|-------------------------|
|Language       |Python 3.x               |
|Agent Framework|LangChain / LlamaIndex   |
|LLM            |OpenAI GPT / Groq / Other|
|Vector Store   |FAISS / ChromaDB         |
|Embeddings     |OpenAI / HuggingFace     |
|Frontend       |Streamlit                |
|Config         |python-dotenv            |

-----

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/veeravallisarathkumar/Agentic-RAG.git
cd Agentic-RAG
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
# Add any other required API keys
```

### 4. Add Your Documents

Place your documents (PDF, TXT, etc.) into the `data/` directory.

### 5. Run the Application

```bash
streamlit run streamlit_app.py
```

Then open your browser at `http://localhost:8501` and start asking questions!

-----

## 💡 Example Use Cases

- **Document Q&A** — Upload research papers, reports, or manuals and ask questions in plain English
- **Knowledge Base Chat** — Turn your internal documents into a conversational assistant
- **Multi-step Reasoning** — Ask questions that require combining information from multiple sources

-----

## 🧑‍💻 Skills Demonstrated

This project showcases hands-on experience with:

- ✅ **Agentic AI design** — building systems where LLMs autonomously drive retrieval and reasoning
- ✅ **RAG pipeline engineering** — document ingestion, chunking, embedding, and vector search
- ✅ **LLM integration** — working with OpenAI APIs and prompt engineering
- ✅ **Full-stack AI apps** — connecting a backend agent pipeline to a Streamlit frontend
- ✅ **Python best practices** — modular code structure, environment management, reproducibility

-----

## 📬 Contact

**Veeravalli Sarath Kumar**

- GitHub: [@veeravallisarathkumar](https://github.com/veeravallisarathkumar)

-----

> *Built to explore the frontier of agentic AI systems — where LLMs don’t just answer, they reason.*
