import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


load_dotenv()


print("Loading PDFs from the data directory...")
loader = PyPDFDirectoryLoader("./data")
documents = loader.load()
print(f"Loaded {len(documents)} pages of content.")


print("Chunking documents into smaller pieces...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200 
)
chunks = text_splitter.split_documents(documents)
print(f"Split documents into {len(chunks)} chunks.")


print("Generating embeddings and storing in Chroma database...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

print("Success! Database populated with real PDF data.")