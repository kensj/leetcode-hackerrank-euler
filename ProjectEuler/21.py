import timeit

def euler_21(ceil):
    total = []
    for num in range(1, ceil):
        d_a = sum(get_factors(num))
        d_b = sum(get_factors(d_a))
        if d_b == num and num < d_a: 
            total.append(num)
            total.append(d_a)

    return sum(total)
    
def get_factors(n):
    nums = []
    for i in range(1, int(n**0.5)+1):
        if not n%i: 
            if n/i == i:
                nums.append(i)
            else:
                nums.extend((int(n/i), i))
    if n in nums:
        nums.remove(n)
    return nums

if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_21(10000)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
