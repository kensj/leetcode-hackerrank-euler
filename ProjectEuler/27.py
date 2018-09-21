import timeit

def euler_27():
    max_n = 0
    max_a = 0
    max_b = 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(abs(quad(n, a, b))):
                n += 1
            if n > max_n:
                max_n = n
                max_a = a
                max_b = b

    return max_a*max_b

def quad(n, a, b):
    return int((n*n) + a*n + b)

def is_prime(n):
    primes = []
    for x in range(1, int(n**0.5)+1):
        if not n % x:
            if n/x == x:
                primes.append(x)
            else:
                primes.extend((int(n/x), x))
    if len(primes) <= 2:
        return True
    return False

if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_27()
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
