import math
import timeit

def euler_25(n):
    fib = [1, 1]
    i = 2
    while digits(fib[-1]) < n:
        num = fib[i-1] + fib[i-2]
        fib.append(num)
        i += 1

    return i

def digits(n):
    return int(math.log10(n))+1

if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_25(1000)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
