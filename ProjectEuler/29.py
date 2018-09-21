import timeit

def euler_29(n):
    nums = set()
    for a in range(2, n+1):
        for b in range(2, n+1):
            nums.add(a ** b)

    return len(nums)

if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_29(100)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
