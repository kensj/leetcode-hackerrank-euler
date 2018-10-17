def stepPerms(n):
    ret = [1,1,2] + ([0] * (n-2))
    for x in range(3, n+1): ret[x] = ret[x-1] + ret[x-2] + ret[x-3] 
    return ret[n]