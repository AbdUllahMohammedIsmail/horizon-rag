from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print("=" * 50)
    print(f"Loaded {len(documents)} pages")
    print("=" * 50)

    return documents


if __name__ == "__main__":
    docs = load_pdf(
        "data/Horizon_Tours_Complete_Knowledge_Base_2025.pdf"
    )

    print(docs[0].page_content[:800])