#怎样在一个序列上面保持元素顺序的同时消除重复的值？
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            print(item)
            yield item
            seen.add(item)
            print(seen)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

