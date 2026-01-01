import os
import streamlit as st
from rag_utility import process_document_to_chroma_db, answer_question

working_dir = os.path.dirname(os.path.abspath(__file__))

st.title("🦙 Multi-PDF RAG QA Bot")

uploaded_files = st.file_uploader(
    "Upload multiple PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        save_path = os.path.join(working_dir, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        process_document_to_chroma_db(save_path, uploaded_file.name)

    st.success("All documents processed and added to knowledge base.")

question = st.text_input("Ask a question across all PDFs")

if st.button("Answer"):
    answer, sources = answer_question(question)

    st.markdown("### 🧠 Answer")
    st.write(answer)

    st.markdown("### 📚 Sources")
    for src in sources:
        st.write(f"- {src}")
