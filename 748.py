from collections import Counter
from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate = Counter([c for c in licensePlate.lower() if c.isalpha()])
        ans = ""
        for word in words:
            b = Counter(word)
            a = plate - b
            if (ans == "" or len(word) < len(ans)) and not a:
                ans = word
        return ans


b = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
a = Solution()
o = a.shortestCompletingWord(b, words)
print(o)

def answer(license, words):
    l = Counter([i for i in license.lower() if i.isalpha()])
    ans = ''
    for i in words:
        b = Counter(i) - l
        if not b and ans == '':
            ans = i
    return ans

a = "1s3 PSt"
b = ["step","steps","stripe","stepple"]

print(answer(a,b))