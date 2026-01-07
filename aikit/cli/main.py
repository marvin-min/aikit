"""
CLI 主入口
"""
import click
import sys
from ..core.config import Config
from ..utils.logger import setup_logger

# 设置日志
logger = setup_logger("aikit")


@click.group()
@click.option('--verbose', '-v', is_flag=True, help='启用详细日志')
def cli(verbose):
    """AI Kit - 人工智能工具集合"""
    if verbose:
        logger.setLevel('DEBUG')
        logger.debug("已启用详细日志模式")
    
    # 验证配置
    if not Config.validate():
        sys.exit(1)


@cli.command()
def version():
    """显示版本信息"""
    from .. import __version__
    click.echo(f"aikit v{__version__}")


# 导入工具命令
from .commands.summarize import summarize_command
cli.add_command(summarize_command, name='summarize')


if __name__ == '__main__':
    cli()