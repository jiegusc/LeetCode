from typing import List


def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    return sorted(points, key = lambda y: y[0] ** 2 + y[1] ** 2)[:K]


# return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]
points = [[1,3],[-2,2]]
K = 1
print(kClosest(points, K))