def countSwaps(a):
    #numSwaps = countSwapsFunc(a, 0)
    numSwaps = 0
    for x in range(0, len(a)-1):
        for y in range(x+1, len(a)):
            if a[x] > a[y]:
                a[x], a[y] = a[y], a[x]
                numSwaps = numSwaps + 1
    
    print("Array is sorted in " +str(numSwaps)+ " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
