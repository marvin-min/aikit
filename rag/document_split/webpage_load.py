from langchain_community.document_loaders import WebBaseLoader
from bs4 import SoupStrainer
url = 'https://juejin.cn/post/7571672422689865780'
loader = WebBaseLoader(web_path=[url], bs_kwargs=dict(parse_only = SoupStrainer(id="article-root")))
page = loader.load()
print(page)