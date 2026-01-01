# rag-document-assistant
“Multi-PDF RAG chatbot with source-aware answers.”
🦙 Multi-PDF RAG Question-Answering Bot

A Retrieval-Augmented Generation (RAG) web app that allows users to upload multiple PDF documents and ask questions across all of them.
The system retrieves relevant information from the uploaded documents and uses a Large Language Model to generate grounded, context-aware answers with document source attribution.

Built with Streamlit, LangChain, ChromaDB, HuggingFace Embeddings, and Groq (Llama-3.3-70B).

🚀 Features

📂 Upload multiple PDF files

🔍 Semantic search across all documents

🧠 LLM-powered answers grounded in your data

📚 Source tracking (see which PDFs were used for each answer)

💾 Persistent vector database (ChromaDB)

⚡ Fast inference using Groq’s Llama-3.3-70B

🧩 Architecture

This app implements a full RAG (Retrieval-Augmented Generation) pipeline:

Document Ingestion

PDFs are uploaded through Streamlit

Text is extracted and split into overlapping chunks

Embedding & Storage

Each chunk is embedded using HuggingFace embeddings

Stored in a persistent Chroma vector database

Each chunk keeps metadata about its source PDF

Retrieval

When a question is asked, the vector DB retrieves the most relevant chunks across all PDFs

Generation

Retrieved chunks are passed as context to Llama-3.3-70B

The model generates a grounded answer based only on the retrieved content

Source Attribution

The filenames of the retrieved chunks are displayed below the answer

🖥️ Demo Flow

Upload 2–3 PDF files

Ask a question that may require information from more than one document

Get:

A natural language answer

A list of source files used to generate it

🛠️ Tech Stack

Frontend: Streamlit

LLM: Llama-3.3-70B via Groq

Embeddings: HuggingFace

Vector Store: ChromaDB

RAG Framework: LangChain

PDF Parsing: Unstructured

📦 Installation
git clone https://github.com/your-username/multi-pdf-rag.git
cd multi-pdf-rag

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key

▶️ Run the App
streamlit run app.py


Open the local URL shown in the terminal.

🌐 Deploy on Streamlit Cloud

Push this repository to GitHub

Go to https://share.streamlit.io

Connect your GitHub repo

Set your GROQ_API_KEY in Streamlit Secrets

Click Deploy 🚀

🎯 Use Cases

Research assistants

Legal or policy document Q&A

Academic paper exploration

Company internal knowledge bases

Hackathon or AI demo projects

📌 Why RAG?

RAG allows LLMs to:

Use your data

Avoid hallucinations

Provide verifiable, document-grounded answers

This project demonstrates a real, production-style RAG pipeline with multi-document support.

👩‍💻 Author

Leen
AI Engineer | GenAI & RAG Systems
Building intelligent systems that turn documents into knowledge.
