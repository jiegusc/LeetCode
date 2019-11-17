from collections import deque


def predictPartyVictory(senate: str) -> str:
    D = deque()
    R = deque()
    for i, v in enumerate(senate):
        if v == "D":
            D.append(i)
        else:
            R.append(i)

    n = len(senate)
    while D and R:
        d, r = D.popleft(), R.popleft()
        if d > r:
            R.append(r + n)
        else:
            D.append(d + n)

    return "Dire" if D else "Radiant"

print(predictPartyVictory("RDD"))