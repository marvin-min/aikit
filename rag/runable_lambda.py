
from operator import itemgetter


d = {"foo": "bar", "baz": 123}
ret = itemgetter("baz")(d)
print(ret)