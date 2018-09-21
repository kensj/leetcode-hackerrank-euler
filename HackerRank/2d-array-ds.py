def hourglassSum(arr):
    sums = []
    for x in range(1,5):
        for y in range(1,5):
            top_row = arr[x-1][y-1] + arr[x-1][y] + arr[x-1][y+1]
            middle = arr[x][y]
            bottom_row = arr[x+1][y-1] + arr[x+1][y] + arr[x+1][y+1]
            sums.append(top_row + middle + bottom_row)
    return max(sums)
