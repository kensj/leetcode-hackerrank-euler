def jumpingOnClouds(c):
    start,end,jumps = 0,len(c)-1,0
    while start < end:
        start = start+2 if start+2<=end and c[start+2]==0 else start+1 if start+1<=end and c[start+1]==0 else start
        jumps += 1
    return jumps