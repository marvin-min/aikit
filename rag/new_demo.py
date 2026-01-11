from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
import models

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document

# 示例文档
docs = [
    Document(page_content="LangChain is a framework for building LLM applications."),
    Document(page_content="RAG combines retrieval with generation."),
    Document(page_content="Chroma is a local vector database."),
]

# embedding 模型
embeddings = models.get_embeddings()

# 建立向量库
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
)

# 关键：retriever 就是从 vectorstore 来的
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)
# llm = ChatOpenAI(model="gpt-4o-mini")
client = models.get_client()
prompt = ChatPromptTemplate.from_messages([
    ("system", "Use the context to answer the question.\n\n{context}"),
    ("human", "{question}")
])

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | client
)

print(rag_chain.invoke("What is RAG?").content)
