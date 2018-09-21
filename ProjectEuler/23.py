import timeit

def euler_23():
    abundant = []
    for x in range(1,28123+1):
        num_sum = sum(get_factors(x))
        if num_sum > x:
            abundant.append(x)

    sum_of_abundant = {}
    for x in range(0, len(abundant)):
        for y in range(0, len(abundant)):
            temp_sum = abundant[x] + abundant[y]
            if temp_sum <= 28123:
                sum_of_abundant[temp_sum] = 1

    total = 0
    for x in range(0, 28123+1):
        if x not in sum_of_abundant:
            total += x        

    return total

def get_factors(num):
    nums = []
    for i in range(1, int((num**0.5)+1)):
        if not num % i:
            if num/i == i:
                nums.append(i)
            else:
                nums.extend((int(num/i), i))
            if num in nums:
                nums.remove(num)
    return nums

if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_23()
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  

        
