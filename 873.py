from collections import defaultdict

dp = {i: defaultdict(int) for i in range(10)}

print(dp)


def lenLongestFibSubseq(A):
    """
    :type A: List[int]
    :rtype: int
    """
    dp = {i: defaultdict(int) for i in range(len(A))}
    res = 0
    for i in range(len(A)):
        for j in range(i - 1, - 1, - 1):
            if A[i] in dp[j]:
                dp[i][A[j] + A[i]] = dp[j][A[i]] + 1
                res = max(res, dp[i][A[j] + A[i]])
            else:
                dp[i][A[j] + A[i]] = 2
    return res


