from langchain_community.document_loaders import TextLoader
loader = TextLoader(file_path='./requirements.txt', encoding='utf-8')
documents = loader.load()
print(documents)