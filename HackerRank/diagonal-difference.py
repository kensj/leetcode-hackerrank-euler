def diagonalDifference(arr):
    rows = len(arr)
    cols = len(arr[0])
    forward = 0
    fr = 0
    fc = 0
    while fr < rows:
        forward += arr[fr][fc]
        fr += 1
        fc += 1
    
    backward = 0
    br = 0
    bc = cols-1
    while br < rows:
        backward += arr[br][bc]
        br += 1
        bc -= 1
    return abs(backward-forward)