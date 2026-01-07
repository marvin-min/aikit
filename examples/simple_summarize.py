"""
简单使用示例
"""
from aikit.tools.web_summarizer import WebSummarizer

def main():
    # 创建总结器
    summarizer = WebSummarizer(
        chunk_size=1000,
        chunk_overlap=100,
        retrieval_k=5
    )
    
    # 总结网页
    url = "https://www.active.com/affiliate"
    summary = summarizer.summarize(url, "总结这篇文章的核心内容")
    
    print("📄 总结结果:")
    print(summary)

if __name__ == "__main__":
    main()