def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    # if len(secret) == 1:
    #     if secret[0] == guess[0]:
    #         return "1A0B"
    #     if secret[0] != guess[0]:
    #         return "0A0B"
    # from collections import Counter
    # bull = 0
    # cows = 0
    # index = []
    # b = []
    # c = []
    # for i in range(len(secret)):
    #     if guess[i] == secret[i]:
    #         bull += 1
    #         index.append(i)
    # a = secret
    # d = guess
    # for i in range(len(index)):
    #     b = a.replace(secret[index[i]], '', 1)
    #     c = d.replace(guess[index[i]], '', 1)
    # a = Counter(b)
    # b = Counter(c)
    # for i in a:
    #     if i in a and i in b:
    #         cows += min(a[i], b[i])
    #
    # return str(bull) + "A" + str(cows) + "B"



    bull = 0
    cows = 0
    dup = []
    for i in guess:
        if i in secret and i not in dup:
            cows += min(secret.count(i), guess.count(i))
            dup.append(i)
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            cows -= 1
            bull += 1
    return str(bull) + "A" + str(cows) + "B"


secret = "11"
guess = "11"
a = secret
b = a.replace(secret[1],'')
# print(b)
print(getHint(secret,guess))
