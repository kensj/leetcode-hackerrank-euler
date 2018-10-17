def countingValleys(n, s):
    valley = count = 0
    for x in range(0, n):
        prev = valley
        valley = valley+1 if s[x] == 'U' else valley-1
        if prev == -1 and valley == 0: count += 1
    return count   