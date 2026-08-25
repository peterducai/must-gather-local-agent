from langchain_community.document_loaders import TextLoader
from langchain.tools.retriever import create_retriever_tool
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Load the documentpip install -U "langchain-core"
loader = TextLoader("example.txt")
docs = loader.load()


# Create a vector store and retriever
vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

# Turn it into an agent tool
tool = create_retriever_tool(
    retriever,
    "search_documents",
    "Searches and reads through the loaded text documents.",
)
tools = [tool]