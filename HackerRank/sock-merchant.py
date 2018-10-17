def sockMerchant(n, ar):
    socks,pairs = {},0
    for s in ar: 
        socks[s] = socks.get(s,0)+1
        if socks.get(s,0) == 2: pairs,socks[s] = pairs+1,0
    return pairs