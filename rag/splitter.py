from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=[
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_documents(documents)

    print("=" * 50)
    print(f"Created {len(chunks)} chunks")
    print("=" * 50)

    return chunks


if __name__ == "__main__":
    from loader import load_pdf

    docs = load_pdf(
        "data/Horizon_Tours_Complete_Knowledge_Base_2025.pdf"
    )

    chunks = split_documents(docs)

    print(chunks[0].page_content)

    print("\nMetadata:")
    print(chunks[0].metadata)