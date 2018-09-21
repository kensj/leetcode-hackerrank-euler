def rotLeft(a, d):
    while d > 0:
        a.append(a[0])
        del a[0]
        d = d - 1
    return a
