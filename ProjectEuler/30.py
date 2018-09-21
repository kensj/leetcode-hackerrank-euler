import timeit

def euler_30(n):
    upper_bound = n*(9**n) + 1
    total = 0
    for x in range(2, upper_bound):
        digits = str(x)
        sum_of_exp = 0
        for digit in digits:
            sum_of_exp += int(digit) ** 5
        if sum_of_exp == x:
            total += x
    return total

if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_30(5)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  



