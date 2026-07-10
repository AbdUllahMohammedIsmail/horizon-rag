from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)

question = input("Ask: ")

docs = retriever.invoke(question)

print("\n" + "=" * 80)

for i, doc in enumerate(docs, start=1):

    print(f"\nResult {i}")

    print("-" * 40)

    print(doc.page_content[:700])

    print("\nMetadata:")

    print(doc.metadata)

    print("=" * 80)