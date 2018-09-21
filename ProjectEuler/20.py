import math
import timeit

def euler_20(n):
    digits = str(math.factorial(n))
    total = 0
    for digit in digits:
        total += int(digit)
    return total


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_20(100)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
