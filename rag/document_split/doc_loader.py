from langchain_community.document_loaders import Docx2txtLoader
loader = Docx2txtLoader(file_path='/Users/marvin/Desktop/2026-01.docx')
documents = loader.load()
print(documents)
