import timeit

def euler_9(target):
    for a in range(1, target):
        for b in range(a+1, target):
            # Get a^2 + b^2
            sq = a**2 + b**2
            # Get the square root and truncate if necessary
            c = int(sq ** 0.5)
            # If c^2 = a^2 + b^2 and a+b+c = our target
            if sq == c*c and a+b+c == target:
                return a*b*c


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_9(1000)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runt ime:', stop - start)  

        


