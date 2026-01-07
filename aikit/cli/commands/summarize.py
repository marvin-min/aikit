"""
网页总结命令
"""
import click
from ...tools.web_summarizer.summarizer import WebSummarizer
from ...utils.logger import get_logger

logger = get_logger(__name__)


@click.command()
@click.argument('url')
@click.option('--query', '-q', default='总结这篇文章的核心内容', help='自定义查询问题')
@click.option('--chunk-size', default=1000, help='文档切分大小')
@click.option('--chunk-overlap', default=100, help='文档切分重叠')
@click.option('--retrieval-k', default=5, help='检索文档数量')
@click.option('--output', '-o', type=click.Path(), help='输出到文件')
@click.option('--provider', '-p', type=click.Choice(['dashscope', 'siliconflow'], case_sensitive=False), help='指定 AI 服务商 (dashscope=千问, siliconflow=硅基流动)')
def summarize_command(url, query, chunk_size, chunk_overlap, retrieval_k, output, provider):
    """总结网页内容

    URL: 要总结的网页地址
    """
    try:
        summarizer = WebSummarizer(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            retrieval_k=retrieval_k,
            provider=provider
        )
        
        summary = summarizer.summarize(url, query)
        
        # 输出结果
        header = "📄 AI 总结结果"
        separator = "=" * 30
        result = f"\n{header} {separator}\n{summary}\n"
        
        if output:
            with open(output, 'w', encoding='utf-8') as f:
                f.write(result)
            click.echo(f"✅ 总结已保存到: {output}")
        else:
            click.echo(result)
            
    except Exception as e:
        logger.error(f"❌ 总结失败: {e}")
        raise click.ClickException(f"总结失败: {e}")