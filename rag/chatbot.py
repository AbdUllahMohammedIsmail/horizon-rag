import os

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.output_parsers import StrOutputParser

from rag.config import *
from rag.prompt import PROMPT

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

vectorstore = Chroma(
    persist_directory=VECTOR_DB_PATH,
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10
    }
)

llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=0
)

parser = StrOutputParser()

chain = PROMPT | llm | parser


def ask(question: str):

    docs = retriever.invoke(question)

    context = ""

    pages = []

    for doc in docs:

        page = doc.metadata["page"] + 1

        pages.append(page)

        context += f"""
Page: {page}

Content:
{doc.page_content}

-------------------------------------
"""

    answer = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return answer, sorted(set(pages))


if __name__ == "__main__":

    while True:

        question = input("\nQuestion: ")

        if question.lower() in ["exit", "quit"]:
            break

        answer, pages = ask(question)

        print("\n" + "=" * 80)

        print(answer)

        print(f"\nPages: {pages}")