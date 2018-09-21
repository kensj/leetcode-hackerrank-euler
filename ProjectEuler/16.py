import timeit

def euler_16(exp):
    num = str(2 ** exp)
    total = 0
    for x in num:
        total += int(x)
    return total


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_16(1000)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
