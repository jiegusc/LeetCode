from typing import List
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        res.append(intervals[0])
        for idx in range(1, len(intervals)):
            last = res[-1]
            if last[1] >= intervals[idx][0]:
                last[1] = max(last[1], intervals[idx][1])
            else:
                res.append(intervals[idx])
            idx += 1
        return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = sorted(intervals, key=lambda x: x[0])
# print(intervals)

#
# def solution(A):
#     # write your code in Python 3.6
#     if len(A) == 1:
#         if A[0] <= 0:
#             return 1
#         elif A[0] == 1:
#             return 2
#         else:
#             return A[0] - 1
#     c = sorted(A)
#     if c[0] > 1:
#         return 1
#     for i in range(1,len(c)):
#         diff = c[i] - c[i -1]
#         if diff == 0:
#             pass
#         elif diff != 1 and c[i - 1] < 0:
#             return 1
#         elif diff != 1 and c[i - 1] > 0:
#             return c[i - 1] + 1
#     return c[-1] + 1
#


a = [1, 3, 6, 4, 1, 2]
# print(solution(a))

# b = bin(6)[2:]
# print(b)
# print(b.count("1"))
# print(len(b))


# def solution(N):
#     # write your code in Python 3.6
#     bin_num = bin(N)[2:]
#
#     if bin_num.count("1") == 1:
#         return 0
#     length = len(bin_num)
#
#     restart = 0
#     g_num = 0
#     max_num = 0
#     for i in range(0, len(bin_num)):
#         if bin_num[i] == '0' and restart:
#             g_num += 1
#             if g_num > max_num:
#                 max_num = g_num
#         if bin_num[i] == '1':
#             restart = 1
#             g_num = 0
#
#     return max_num


# def merge(intervals: List[List[int]]) -> List[List[int]]:
#     if not intervals:
#         return intervals
#     result = [intervals[0]]
#     intervals = sorted(intervals, key=lambda x: x[0])
#     i = 1
#     while i < len(intervals):
#         if intervals[i][0] <= result[-1][1]:
#             result[-1][1] = max(intervals[i][1], result[-1][1])
#         else:
#             result.append(intervals[i])
#         i += 1
#     return result
#
#
# b = [[1,4],[0,4]]
#
# print(merge(b))