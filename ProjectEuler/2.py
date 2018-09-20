import timeit

def euler_2():
    total = 0
    # Indexes x, x+1, x+2
    fib_a = 1
    fib_b = 1
    fib_c = 2
    while fib_c < 4000000:
        # Calculate fib[x] + fib[x+1] to get fib[x+2]
        fib_c = fib_a + fib_b
        # If fib[x+2] is even, add it
        if not fib_c%2:
            total += fib_c
        # fib[x] is now fib[x+1]
        fib_a = fib_b
        # fib[x+1] is now fib[x+2]
        fib_b = fib_c
    return total


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_2()
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runt ime:', stop - start)  
