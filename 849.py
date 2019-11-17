def maxDistToClosest(seats):
    """
    :type seats: List[int]
    :rtype: int
    """

    if not seats:
        return 0
    max_len = seats.index(1)
    current_len = 0
    for i in range(max_len + 1, len(seats)):
        if seats[i] == 1:
            max_len = max(max_len, current_len)
            current_len = 0
        else:
            current_len += 1
    return max(current_len, max_len)

a = [1, 0, 0, 1]
print(maxDistToClosest(a))






# def try1(seats):
#     if not seats:
#         return 0
#     result = {}
    # max = 0
    #
    # for i in range(len(seats)):
    #     if seats[i] == 1:
    #         pass
    #     else:
    #         stop = True
    #         j = 0
    #         len_max = 0
    #         while stop:
    #             try:
    #                 if seats[i - j] == 1 or seats[i + j] == 1:
    #                     stop = False
    #                     if len_max > max:
    #                         max = len_max
    #                     if len_max in result:
    #                         pass
    #                     else:
    #                         result[len_max] = i
    #                 else:
    #                     len_max += 1
    #                     j += 1
    #             except:
    #                 if len_max > max:
    #                     max = len_max
    #                 if len_max in result:
    #                     pass
    #                 else:
    #                     result[len_max] = i
    #
    # return result[max]
