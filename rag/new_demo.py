import models

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

# 1️⃣ 初始化模型
client = models.get_client()
embeddings = models.get_embeddings()

# 2️⃣ 加载文档（与旧代码一致）
loader = WebBaseLoader(
    web_path="https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_2a65998b79af47eaaf2115ef1ce234f9.html"
)
docs = loader.load()

# 3️⃣ 向量库
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
)

# 4️⃣ retriever（和旧代码一模一样）
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# 5️⃣ 等价于 chain_type="stuff" 的 prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Use the following context to answer the question.\n\n{context}"),
    ("human", "{question}")
])

# 6️⃣ 等价于 stuff 的 documents 拼接逻辑
def format_docs(docs: list[Document]) -> str:
    return "\n\n".join(doc.page_content for doc in docs)

# 7️⃣ LCEL RAG Chain（完全等价）
rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | client
)

# 8️⃣ 调用（注意：新 API 直接传字符串）
result = rag_chain.invoke(
    "2026年购买一个15万元的纯油车，我能获得多少补贴？"
)

print(result.content)
