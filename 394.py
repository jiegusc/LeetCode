# class Solution(object):
#     def recursion(self, inner_str, reps):
#         if not "[" in inner_str:
#             return inner_str * reps
#         else:
#             return self.decodeString(inner_str) * reps
#
#     def decodeString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         # Example case: s = "3[a2[c]]"
#
#         finalstr = ""
#         numstr = ""
#         i = 0
#         while i < len(s):
#             # check if this character is neither a digit nor a bracket
#             if not s[i].isdigit() and s[i] not in ["[", "]"]:
#                 # this can be added directly to the final string
#                 # since the strings inside the brackets will be handled separately
#                 finalstr += s[i]
#                 i += 1
#                 continue
#
#             else:
#                 if s[i].isdigit():
#                     numstr += s[i]
#                 else:
#                     # this MUST be the starting bracket based on problem description
#                     # find the ending bracket. Make sure to avoid stopping
#                     # at a nested ending bracket
#                     open_brackets = 1
#                     # convert number of repetitions to integer
#                     reps = int(numstr)
#
#                     for k in range(i + 1, len(s)):
#                         if s[k] == "[":
#                             open_brackets += 1
#                         elif s[k] == "]":
#                             open_brackets -= 1
#                             if open_brackets == 0:
#                                 # this is the ending bracket we want
#                                 finalstr += self.recursion(s[(i + 1): k], reps)
#                                 numstr = ""
#                                 i = k
#                                 break
#             i += 1
#         return finalstr

class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ''
        i = 0
        decode = ''
        times = ''
        while i < len(s):
            if not s[i].isdigit() and s[i] not in ['[', ']']:
                decode += s[i]
            else:
                if s[i].isdigit():
                    times += s[i]
                else:
                    start = 0
                    for j in range(i, len(s)):

                        if s[j] == '[':
                            #   start begin
                            start += 1
                        elif s[j] == ']':
                            start -= 1
                        if start == 0:
                            decode += self.decodeString(s[i + 1:j]) * int(times)
                            i = j
                            times = ''
                            break
            i += 1
        return decode









s = "100[leetcode]"
p = decodeString1(s)
print(p)
