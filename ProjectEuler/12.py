import timeit

def euler_12(n):
    x = n    
    while divisors_of_triangle_number(x) <= n:
        x += 1
    return triangle_number(x)

def divisors_of_triangle_number(num):
    if num % 2 == 0:
        return count_factors(num // 2) * count_factors(num + 1)
    else:
        return count_factors((num + 1) // 2) * count_factors(num)
    
def triangle_number(num):
    return (num * (num + 1) // 2)

def count_factors(num):
    count = 2
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            count += 2
    return count

if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_12(500)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
