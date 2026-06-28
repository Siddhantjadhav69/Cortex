# Cortex

A retrieval based question answering system that reads your documents and actually understands what you're asking about.

## What is this?

Cortex lets you upload documents (PDFs, markdown, text files) and then ask questions about them. Instead of keyword searching, it understands the meaning of your question and finds the most relevant parts of your documents. Then it uses an LLM to generate an answer and tells you exactly where that answer came from.

Think of it like having a smart librarian who reads all your books, understands what you're asking, finds the right passages, and explains the answer to you in context.

## Why build this?

Every company doing something interesting with LLMs is building something like this. It's not sexy but it's how you actually make language models useful for real work. They built internal knowledge bases, customer support systems, document analysis tools. All of them use retrieval augmented generation under the hood.

For me, this project touches every part of the AI engineering stack. Vector databases, embeddings, LLM APIs, prompt engineering, data pipelines, REST APIs, Docker, evaluation metrics. It's not a tutorial project. It's the real deal.

## The Stack

**Backend & APIs**
+ FastAPI for the REST server
+ Docker for containerization
+ Redis for caching repeated queries
+ Async Python with asyncio

**LLM & Embeddings**
+ Claude API (via Anthropic) for answer generation
+ HuggingFace sentence transformers for embeddings
+ Support for local models via Ollama

**Data & Storage**
+ Chroma or Pinecone for vector database
+ PyPDF2 and pdfplumber for document parsing
+ LangChain for orchestration

**Quality & Testing**
+ Pytest for unit and integration tests
+ LangSmith for tracing and debugging
+ Custom evaluation metrics for retrieval and generation quality

**Frontend (optional)**
+ React or Streamlit for the UI
+ Fetch API for backend communication

## How it Works

1. You upload documents to Cortex
2. It chunks them into meaningful pieces
3. It generates embeddings for each chunk (storing them in a vector database)
4. When you ask a question, it embeds your question too
5. Finds the most similar chunks using semantic search
6. Sends those chunks plus your question to an LLM
7. The LLM generates an answer with source citations

Simple flow but the engineering decisions around chunking, retrieval ranking, prompt design, and error handling are what separate a toy from something production ready.

## Getting Started

```bash
git clone https://github.com/siddhantjadhav69/cortex.git
cd cortex
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your API keys:
```
ANTHROPIC_API_KEY=your_key_here
PINECONE_API_KEY=your_key_here
```

Run the server:
```bash
uvicorn main:app --reload
```

Now hit `http://localhost:8000/docs` to see the API docs.

## API Endpoints

**POST /documents/upload**
Upload a document and it gets indexed immediately.

**POST /query**
Ask a question. You get back an answer and the source chunks.

**GET /documents**
List all indexed documents.

**DELETE /documents/{doc_id}**
Remove a document from the index.

## What it Can Do

+ Handle PDFs, markdown, and plain text
+ Find answers in thousands of documents
+ Show you exactly where answers came from
+ Cache queries so you're not paying for embeddings twice
+ Run locally with Ollama or hit cloud APIs
+ Handle real edge cases like documents that are too long or questions that don't match anything

## What it Can't Do (Yet)

+ Multi-hop reasoning (questions that need to combine info from different documents)
+ Real time document updates (have to re-index)
+ Complex multi-modal search (images, tables)
+ Streaming responses (though this is on the roadmap)

## The Engineering Challenges

The fun part is that there's no single right way to do any of this:

1. How do you chunk documents? Fixed size? Semantic overlap? Recursive chunking?
2. Which embedding model? Local? Cloud? How do you trade latency for quality?
3. Retrieval ranking. Do you use simple cosine similarity or do you rerank results?
4. How do you handle hallucinations? Prompt engineering? Confidence thresholds?
5. Scaling. What happens when you have a million documents?

These aren't academic questions. They're real problems that change how the system performs.

## Evaluation

There's a benchmark directory with hand labeled question answer pairs. Running evaluation tells you:

+ Retrieval precision and recall (are we finding the right documents?)
+ Answer quality (is the generated answer correct?)
+ Latency and cost per query
+ Failure mode analysis (what kinds of questions break it?)

## Running it in Docker

```bash
docker build -t cortex:latest .
docker run -p 8000:8000 --env-file .env cortex:latest
```

## Project Structure

```
cortex/
├── app/
│   ├── api/
│   │   ├── documents.py
│   │   └── query.py
│   ├── core/
│   │   ├── embedding.py
│   │   ├── retrieval.py
│   │   └── generation.py
│   └── main.py
├── data/
│   ├── documents/
│   └── benchmark/
├── tests/
├── docker/
├── requirements.txt
└── README.md
```

## Next Steps

This is phase 1. Roadmap includes:

+ Streaming responses for faster perceived latency
+ Support for structured data (tables, metadata)
+ Multi-query expansion for harder questions
+ Fine tuning on your domain specific data
+ Web UI
+ Multi user support with auth

## Contributing

This is my learning project but if you spot bugs or have ideas, open an issue.

## License

MIT. Do whatever you want with it.

---

Built to understand what's actually possible at the intersection of retrieval and generation. Not fancy. Just works.
