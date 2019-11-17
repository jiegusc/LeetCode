from typing import List
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if not flowerbed:
        return False
    ok, set1 = 0, 1
    for i in flowerbed:
        if i :
            set1 = 0
        else:
            set1 += 1
        if set1 == 3:
            ok += 1
            set1 = 1
    if set1 == 2: ok += 1
    return ok >= n

flowerbed = [1,0,0,0,1]
n = 2

print(canPlaceFlowers(flowerbed, n))
