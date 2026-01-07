"""
网页总结工具 - 主要逻辑
"""
import bs4
from typing import List, Dict, Any

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

from ...core.models import get_client, get_embeddings
from ...core.config import Config
from ...utils.logger import get_logger
from ...utils.helpers import truncate_text

logger = get_logger(__name__)


class WebSummarizer:
    """网页内容总结工具"""

    def __init__(self, chunk_size: int = None, chunk_overlap: int = None, retrieval_k: int = None, provider: str = None):
        self.chunk_size = chunk_size or Config.DEFAULT_CHUNK_SIZE
        self.chunk_overlap = chunk_overlap or Config.DEFAULT_CHUNK_OVERLAP
        self.retrieval_k = retrieval_k or Config.DEFAULT_RETRIEVAL_K
        self.provider = provider
        self.logger = logger
    
    def load_documents(self, url: str) -> List[Any]:
        """加载网页文档"""
        self.logger.info(f"🚀 开始处理 URL: {url}")
        
        try:
            loader = WebBaseLoader(web_path=url)
            docs = loader.load()
            
            if not docs or not docs[0].page_content.strip():
                self.logger.warning("⚠️ 无法获取内容，尝试全页面抓取...")
                loader.bs_kwargs = {}
                docs = loader.load()
            
            return docs
        except Exception as e:
            self.logger.error(f"❌ 文档加载失败: {e}")
            raise
    
    def split_documents(self, docs: List[Any]) -> List[Any]:
        """切分文档"""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        documents = text_splitter.split_documents(docs)
        self.logger.info(f"✅ 文档已切分为 {len(documents)} 个片段")
        return documents
    
    def create_vector_store(self, documents: List[Any]):
        """创建向量存储"""
        vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=get_embeddings(self.provider)
        )
        return vectorstore
    
    def create_chain(self):
        """创建RAG链"""
        retriever = self.create_vector_store([]).as_retriever(
            search_kwargs={"k": self.retrieval_k}
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "你是一个专业的文案总结助手。请根据以下上下文内容进行总结。\n\n上下文：\n{context}"),
            ("user", "任务：{input}\n\n注意：请分条目列出核心要点,保持客观准确。"),
        ])
        
        combine_docs_chain = create_stuff_documents_chain(get_client(), prompt)
        rag_chain = create_retrieval_chain(retriever, combine_docs_chain)
        
        return rag_chain
    
    def summarize(self, url: str, query: str = "总结这篇文章的核心内容") -> str:
        """总结网页内容"""
        try:
            # 1. 加载文档
            docs = self.load_documents(url)
            
            # 2. 切分文档
            documents = self.split_documents(docs)
            
            # 3. 创建向量存储和检索器
            vectorstore = self.create_vector_store(documents)
            retriever = vectorstore.as_retriever(search_kwargs={"k": self.retrieval_k})
            
            # 4. 创建RAG链
            prompt = ChatPromptTemplate.from_messages([
                ("system", "你是一个专业的文案总结助手。请根据以下上下文内容进行总结。\n\n上下文：\n{context}"),
                ("user", "任务：{input}\n\n注意：请分条目列出核心要点,保持客观准确。"),
            ])
            
            combine_docs_chain = create_stuff_documents_chain(get_client(provider=self.provider), prompt)
            rag_chain = create_retrieval_chain(retriever, combine_docs_chain)
            
            # 5. 调试信息：显示检索到的片段
            relevant_docs = retriever.invoke(query)
            self.logger.info("\n[Debug] 检索到的原始片段预览:")
            for i, doc in enumerate(relevant_docs):
                content_snippet = truncate_text(doc.page_content, 60)
                self.logger.info(f"  [{i}] {content_snippet}")
            
            # 6. 执行总结
            self.logger.info("✍️ 正在生成总结报告...")
            result = rag_chain.invoke({"input": query})
            
            return result["answer"]
            
        except Exception as e:
            self.logger.error(f"❌ 总结过程出错: {e}")
            raise