from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from rag.loader import load_pdf
from rag.splitter import split_documents

def create_vectorstore():
    # تحميل الـ PDF
    docs = load_pdf("data/Horizon_Tours_Complete_Knowledge_Base_2025.pdf")

    # تقسيمه إلى Chunks
    chunks = split_documents(docs)

    # نموذج الـ Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    # إنشاء قاعدة البيانات
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    print("=" * 50)
    print("✅ Vector Database Created Successfully!")
    print("=" * 50)

    return vectorstore


if __name__ == "__main__":
    create_vectorstore()