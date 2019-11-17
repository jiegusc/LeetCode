def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    # ver1 = [int(i) for i in version1.split('.')]
    # ver2 = [int(i) for i in version2.split('.')]
    # while len(ver1) > 0:
    #     if ver1[-1] == 0:
    #         del ver1[-1]
    #     else:
    #         break
    # while len(ver2) > 0:
    #     if ver2[-1] == 0:
    #         del ver2[-1]
    #     else:
    #         break
    # v1 = int(''.join(map(str,ver1)))
    # v2 = int(''.join(map(str,ver2)))
    # if v1 > v2:
    #     return 1
    # if v1 < v2:
    #     return -1
    # else:
    #     return 0

    ver1 = [int(i) for i in version1.split('.')]
    ver2 = [int(i) for i in version2.split('.')]
    if len(ver1) > len(ver2):
        ver2.extend([0] * (len(ver1) - len(ver2)))
    if len(ver2) > len(ver1):
        ver1.extend([0] * (len(ver2) - len(ver1)))
    ver1 = int(''.join(map(str, ver1)))
    ver2 = int(''.join(map(str, ver2)))
    if ver1 > ver2 :
        return 1
    if ver1 < ver2:
        return -1
    else:
        return 0

# def delete0(version):
#     while version[-1] == 0 and

ver1 = "1"
ver2 = "0"

ver3 = '0.1'
ver4 = '0.0.1'
print(compareVersion(ver3,ver4))

a = [1,2,3]
b = int(''.join(map(str,a)))
print(b)