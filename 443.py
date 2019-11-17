def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    if not chars:
        return 0
    l = []
    count = 1
    char = ''
    for i in range(len(chars)):
        if chars[i] == char:
            count += 1
        else:
            char = chars[i]
            if count > 1:
                if count < 10:
                    l.append(str(count))
                else:
                    a = list(map(str, str(count)))
                    for i in a:
                        l.append(i)
            l.append(char)
            count = 1
    if count > 1:
        if count < 10:
            l.append(str(count))
        else:
            a = list(map(str, str(count)))
            for i in a:
                l.append(i)
    return l

input = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(input))

