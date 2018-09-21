import timeit

def euler_26(n):
    prime = []
    for x in range(7, n, 2):
        primes = []
        for y in range(1, int(x**0.5)+1):
            if not x % y:
                if x/y == y:
                    primes.append(y)
                else:
                    primes.extend((int(x/y), y))
        if len(primes) <= 2:
            prime.append(x)

    longest = 0
    for num in prime:
        p = 1
        while (10 ** p) % num != 1:
            p += 1
        if p > longest:
            longest = p+1

    return longest


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_26(1000)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
