A = 'absdf'
B = 'absgh'
b = 'abcd'
m = 'abcd'

# c = [i for i in range(len(A)) if A[i] != B[i]]
# print(type(c[0]))

def buddyStrings(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    if len(A) != len(B):
        return False
    c = [i for i in range(len(A)) if A[i] != B[i]]
    if len(c) == 0:
        if len(A) > len(set(A)):
            return True
        else:
            return False

    if len(c) == 2 and A[c[0]] == B[c[1]] and A[c[1]] == B[c[0]]:
        return True
    return False


print(buddyStrings(b,m))