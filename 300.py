def lengthOfLIS(nums):
    if not nums: return 0
    dp=[1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            a = nums[j]
            b = nums[i]
            c = dp[i]
            d = dp[j]
            if a < b and d+1>c:
                dp[i]=dp[j]+1
    return max(dp)



a = [10,9,2,5,3,7,101,18]

print(lengthOfLIS(a))

