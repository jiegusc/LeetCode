class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        count = 0
        last_seen = {}

        for i, c in enumerate(s):
            count += 1
            if c in last_seen:
                count = min(count, i - last_seen[c])
            last_seen[c] = i
            longest = max(count, longest)

        return longest


def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    count = 0
    result = {}
    for i in range(len(s)):
        count += 1
        if s[i] in result:
            count = min(count, i - result[s[i]])
        result[s[i]] = i
        longest = max(longest, count)
    return longest


a = "au"
print(lengthOfLongestSubstring(a))
