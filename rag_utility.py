import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_chroma import Chroma

load_dotenv()

working_dir = os.path.dirname(os.path.abspath(__file__))
VECTOR_DB_DIR = f"{working_dir}/doc_vectorstore"

embedding = HuggingFaceEmbeddings()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)

def get_vectordb():
    return Chroma(
        persist_directory=VECTOR_DB_DIR,
        embedding_function=embedding
    )

def process_document_to_chroma_db(file_path, file_name):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Add filename as metadata
    for doc in documents:
        doc.metadata["source"] = file_name

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)

    vectordb = get_vectordb()
    vectordb.add_documents(chunks)

def answer_question(user_question):
    vectordb = get_vectordb()
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})

    docs = retriever.invoke(user_question)


    context = ""
    sources = set()

    for doc in docs:
        context += doc.page_content + "\n\n"
        sources.add(doc.metadata.get("source"))

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{user_question}
"""

    response = llm.invoke(prompt)

    return response.content, list(sources)
