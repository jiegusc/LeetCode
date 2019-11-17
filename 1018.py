def prefixesDivBy5(A):
    """
    :type A: List[int]
    :rtype: List[bool]
    """
    A = ''.join(str(i) for i in A)
    result_list = []
    for i in range(1, len(A) + 1):
        result_list.append(int(A[:i],2) % 5 == 0)
    return result_list


print(prefixesDivBy5([0,1,1]))