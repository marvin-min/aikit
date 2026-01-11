import models
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain.chains.retrieval_qa.base import RetrievalQA
# 1. 初始化嵌入模型
client = models.get_client()
# 获取嵌入模型
embeddings = models.get_embeddings()
# 2. 加载要处理的文档
webPageLoader = WebBaseLoader(web_path="https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_2a65998b79af47eaaf2115ef1ce234f9.html")
doc = webPageLoader.load()
# print(doc)

# 3. 创建向量存储
db = Chroma.from_documents(documents=doc, embedding=embeddings)

# 4. 构建检索链
retriever = db.as_retriever(search_kwargs={"k": 3})

qa_chain = RetrievalQA.from_chain_type(
    llm=client,
    chain_type="stuff",
    retriever=retriever
)

# 5. 执行查询
response = qa_chain.invoke({"query": "2026年买一个15万元的纯油车，我能获得多少补贴？"})
print(response)