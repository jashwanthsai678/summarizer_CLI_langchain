from langchain import HuggingFaceHub
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter

def create_qa(notes: str):
    embeddings = HuggingFaceEmbeddings()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([notes])
    vectorstore = FAISS.from_documents(docs, embeddings)

    retriever = vectorstore.as_retriever()
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-small",
        model_kwargs={"temperature": 0.0, "max_length": 256}
    )
    qa = RetrievalQA.from_chain_type(llm, retriever=retriever)
    return qa
