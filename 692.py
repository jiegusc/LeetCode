from typing import List
from collections import Counter


def topKFrequent(words: List[str], k: int) -> List[str]:
    a = Counter(words)
    result = []
    b = sorted(a.items(), key = lambda x: x[0])
    n = sorted(b, key = lambda x: x[1], reverse = True)
    # g = b.most_common()
    # for i in range(k):
    #     result.append(g[i][0])

    return n[:k]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3

# print(topKFrequent(words, k))
# a = Counter(words)
# print(a.items())
# print(a)
# b = sorted(a)
# print(b)
# print("#" * 86)
# c = sorted(a.items(), key= lambda x: x[0])
# print(c)
# d = sorted(c, key=lambda x:x[1])
# print(d)
#
# e = sorted(b, key=lambda x:x[1])
# print(e)
