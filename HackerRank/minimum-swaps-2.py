def minimumSwaps(arr):
    swaps = 0
    x = 0
    while x < len(arr)-1:
        if arr[x] == x+1 or x < 0:
            x += 1
            continue
        y = arr[x]-1
        arr[x], arr[y] = arr[y], arr[x]
        swaps += 1
        x -= 1
    return swaps