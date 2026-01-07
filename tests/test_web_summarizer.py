"""
网页总结工具的测试
"""
import pytest
from unittest.mock import Mock, patch
from aikit.tools.web_summarizer.summarizer import WebSummarizer

class TestWebSummarizer:
    """网页总结工具测试"""
    
    def setup_method(self):
        """测试前准备"""
        self.summarizer = WebSummarizer(
            chunk_size=500,
            chunk_overlap=50,
            retrieval_k=3
        )
    
    @patch('aikit.tools.web_summarizer.summarizer.WebBaseLoader')
    @patch('aikit.tools.web_summarizer.summarizer.Chroma')
    @patch('aikit.tools.web_summarizer.summarizer.get_client')
    @patch('aikit.tools.web_summarizer.summarizer.get_embeddings')
    def test_summarize_success(self, mock_embeddings, mock_client, mock_chroma, mock_loader):
        """测试成功总结"""
        # Mock 加载器
        mock_docs = [Mock(page_content="测试内容这是测试文章内容")]
        mock_loader.return_value.load.return_value = mock_docs
        
        # Mock 向量存储
        mock_vectorstore = Mock()
        mock_retriever = Mock()
        mock_retriever.invoke.return_value = [
            Mock(page_content="检索到的内容1"),
            Mock(page_content="检索到的内容2")
        ]
        mock_vectorstore.as_retriever.return_value = mock_retriever
        mock_chroma.from_documents.return_value = mock_vectorstore
        
        # Mock 客户端
        mock_chain = Mock()
        mock_chain.invoke.return_value = {"answer": "测试总结"}
        
        with patch('aikit.tools.web_summarizer.summarizer.create_retrieval_chain') as mock_rag:
            mock_rag.return_value = mock_chain
            with patch('aikit.tools.web_summarizer.summarizer.create_stuff_documents_chain') as mock_docs:
                mock_docs.return_value = mock_chain
                
                result = self.summarizer.summarize("https://example.com")
                
                assert result == "测试总结"
                mock_loader.assert_called_once()
    
    def test_init_with_custom_params(self):
        """测试自定义参数初始化"""
        custom_summarizer = WebSummarizer(
            chunk_size=1500,
            chunk_overlap=200,
            retrieval_k=8
        )
        
        assert custom_summarizer.chunk_size == 1500
        assert custom_summarizer.chunk_overlap == 200
        assert custom_summarizer.retrieval_k == 8