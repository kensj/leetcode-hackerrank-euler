import timeit

def euler_31():
    ways = 0
    for a in range(200, -1, -200):
        for b in range(a, -1, -100):
            for c in range(b, -1, -50):
                for d in range(c, -1, -20):
                    for e in range(d, -1, -10):
                        for f in range(e, -1, -5):
                            for g in range(f, -1, -2):
                                ways += 1

    return ways


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_31()
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
