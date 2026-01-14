from langchain_text_splitters import CharacterTextSplitter

text = "第一段文本内容。这是一个示例，用于测试文本分割功能。\n\n第二段文本内容。它包含更多的信息，以确保分割器能够正确处理多段文本。\n第三段文本内容。最后一段，用于验证分割的完整性。"
splitter = CharacterTextSplitter(separator="\n", chunk_size=10, chunk_overlap=5)
texts = splitter.split_text(text)
for i, text in enumerate(texts):
    print(f"Chunk {i+1}:\n{text}\n")