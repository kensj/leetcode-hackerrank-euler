import timeit

def euler_28(n):
    total = 1
    for x in range(3, n+1, 2):
        total += 4*(x**2) - 6*(x-1)
    return total


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_28(1001)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
