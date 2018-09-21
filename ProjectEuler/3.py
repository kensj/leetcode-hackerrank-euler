import timeit

def euler_3():
    n = 600851475143
    # Start with smallest prime number
    i = 2
    # there exists a number less than n that can be divided by i twice
    while i * i < n:
        # Keep dividing while our number is divisible by factor i
        while not n%i:
            n /= i
        # Check the next one
        i += 1
    # At this point, we can't divide n by any number anymore
    # We end up with the largest prime factor of n
    return n

if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_3()
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
