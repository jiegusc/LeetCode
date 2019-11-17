class Solution:
    def frequencySort(self, s: str) -> str:

        from collections import Counter
        b = Counter(s)
        result = {}
        re = []
        for i in b:
            if b[i] in result:
                result[b[i]] += i
            else:
                result[b[i]] = i
        dic_key_sort = sorted(result.keys(), reverse=True)
        for i in dic_key_sort:
            if len(result[i]) == 1:
                for _ in range(i):
                    re.append(result[i])
            else:
                g = sorted(result[i])
                for j in range(len(g)):
                    for _ in range(i):
                        re.append(result[i][j])
        return ''.join(re)