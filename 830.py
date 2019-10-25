class Solution:
    def largeGroupPositions(self, S: str):
        if not S:
            return []
        start, same = 0, 1
        res = []
        pre = S[0]

        for i in range(1, len(S)):
            if pre == S[i]:
                same += 1
            else:
                if same >= 3:
                    res += (start, i - 1),
                same = 1
                start = i
            pre = S[i]

        if same >= 3:
            res += (start, len(S)-1),

        return res
S = "abcdddeeeeaabbbcd"


