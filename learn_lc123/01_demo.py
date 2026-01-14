from models import get_client
llm = get_client()
resp = llm.invoke("美国有多少个州?")
print(resp)