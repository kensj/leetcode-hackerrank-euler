import timeit

def euler_1():
    total = 0
    for x in range(1000):
        # If x is a multiple of 3 or 5
        if not x%3 or not x%5:
           total += x
    return total


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_1()
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
