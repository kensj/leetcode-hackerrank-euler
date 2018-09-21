import timeit

def euler_15(size):
    paths = 1
    for i in range(0, size):
        paths *= (2*size) - i
        paths /= i + 1
    return int(paths)


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_15(20)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
