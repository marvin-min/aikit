from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
loader = TextLoader(file_path='./rag/document_split/c1.txt', encoding='utf-8')
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50, separators=["\n\n", "\n", " ", ""])
texts = splitter.split_documents(documents)
for i, text in enumerate(texts):
    print(f"Chunk {i+1}:\n{text}\n")