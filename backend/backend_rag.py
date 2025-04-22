from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from loguru import logger  
from langchain.vectorstores import FAISS
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

def get_response(prompt: str) -> str:

    loader = TextLoader("texts/instructions.txt")
    documents = loader.load()
    logger.info(f"Loaded {len(documents)} documents")
    
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(documents, embeddings)
    
    llm = Ollama(model="mistral:instruct")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
    
    response = qa_chain.run(prompt)
    return response