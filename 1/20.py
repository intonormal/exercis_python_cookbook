#现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作， 比如查找值或者检查某些键是否存在。
from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(b,a)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)
#一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。 然后，这些字典并不是真的合并在一起了，

#对于字典的更新或删除操作总是影响的是列表中第一个字典。
c['z'] = 10
print(b)

values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)

ChainMap({'x': 3}, {'x': 2}, {'x': 1})
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
print(values)


merged = dict(b)
merged.update(a)
#如果原字典做了更新，这种改变不会反应到新的合并字典中去
