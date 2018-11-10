def compareTriplets(a, b):
    ret = [0,0]
    for x in range(0, len(a)):
        if a[x]>b[x]: ret[0] += 1
        elif a[x]<b[x]: ret[1] += 1
    return ret
	