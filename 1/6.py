#怎样实现一个键对应多个值的字典（也叫 multidict）？
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d['a'])

d = defaultdict(set)
d['a'].add(1)
d['a'].add(3)
d['b'].add(4)
print(d['a'])
print(d['c']) #defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体。

d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(5)
d.setdefault('b', []).append(4)
print(d['a'])