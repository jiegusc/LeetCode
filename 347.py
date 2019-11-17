from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
    from collections import Counter
    a = Counter(nums)
    key = []
    for c, v in a.most_common():
        key.append(c)
    return key[:k]



nums = [1,2,2,4,5]
k = 2
print(topKFrequent(nums, k))

