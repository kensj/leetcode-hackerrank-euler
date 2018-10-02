def arrayManipulation(n, queries):
    arr = [0] * (n+1)
    for query in queries:
        arr[query[0]-1] += query[2]
        arr[query[1]] -= query[2]
    total = maximum = 0
    for a in arr:
        total += a
        if total > maximum: maximum = total
    return maximum
