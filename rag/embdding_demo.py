
from models import get_embeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
embeddings = get_embeddings()
score_measures = ['default', 'cosine', 'l2', 'ip']
db = Chroma(
  embedding_function=embeddings,
  persist_directory="./chroma_db",
  collection_name="lc123",
  collection_metadata={"hnsw:space": "l2"}
)

documents = [
  Document(page_content="陕西的红富士苹果真是很好吃"),
  Document(page_content="苹果手机真的很好用"),
]
db.add_documents(documents)
docs = db.similarity_search_with_score("我想买点水果")
for doc, score in docs:
  print(f"Score: {score}, Document: {doc.page_content}")