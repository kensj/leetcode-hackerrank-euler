def plusMinus(arr):
    neg = 0
    pos = 0
    neu = 0
    for n in arr:
        if n < 0:
            neg += 1
        elif n == 0:
            neu += 1
        elif n > 0:
            pos += 1
    total = neg + neu + pos
    print(pos/total)
    print(neg/total)
    print(neu/total)
	