#怎样找出一个序列中出现次数最多的元素呢？

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
print(word_counts)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(word_counts.values())
print(top_three)

morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)
print(word_counts.most_common(3))

a = Counter(words)
b = Counter(morewords)
print(a+b)
print(a-b)