# def findNumberOfLIS(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if len(nums) <= 1:
#         return len(nums)
#     dp = [[1, 1] for _ in nums]
#     max_len = 1
#     for i in range(1, len(nums)):
#         for j in range(0, i):
#             if nums[i] > nums[j]:
#                 if dp[i][1] < dp[j][1] + 1:
#                     dp[i] = [dp[j][0], dp[j][1] + 1]
#                 elif dp[i][1] == dp[j][1] + 1:
#                     dp[i][0] += dp[j][0]
#                 max_len = max(max_len, dp[i][1])
#     ans = 0
#     for d in dp:
#         if d[1] == max_len:
#             ans += d[0]
#     return ans


def findNumberOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    dp = [[1, 1] for _ in range(len(nums))]
    max_len = 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[i][1] < dp[j][1] + 1:
                    dp[i] = [dp[j][0], dp[j][1] + 1]
                elif dp[i][1] == dp[j][1] + 1:
                    dp[i][0] += dp[j][0]
                max_len = max(max_len, dp[i][1])
    ans = 0
    for i in dp:
        if i[1] == max_len:
            ans += i[0]

    return ans


a = [2,2,3,2,3]

print(findNumberOfLIS(a))
