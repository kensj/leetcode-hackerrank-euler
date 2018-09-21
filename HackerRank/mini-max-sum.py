def miniMaxSum(arr):
    arr = sorted(arr)
    minimum = arr[0] + arr[1] + arr[2] + arr[3]
    maximum = arr[1] + arr[2] + arr[3] + arr[4]
    print(str(minimum) + ' ' + str(maximum))