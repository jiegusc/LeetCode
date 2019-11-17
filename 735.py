from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    if not asteroids:
        return asteroids

    result, index = [], 0
    while index < len(asteroids):
        #   if is positive, append; if is negative, ignore.
        if asteroids[index] > 0:
            result.append((asteroids[index]))
        #   below is negative of zero(0):
        elif not result or result[-1] < 0:
            result.append((asteroids[index]))
        elif - asteroids[index] < result[-1]:
            pass
        elif - asteroids[index] > result[-1]:
            result.pop()
            index -= 1
        elif - asteroids[index] == result[-1]:
            result.pop()
            pass
        index += 1
    return result


print(asteroidCollision([3,-2, -1, 1, 2]))