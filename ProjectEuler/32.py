import timeit

def euler_32():
    nums = []

    x = ''
    y = 98765
    while(len(str(y)) > 1): 
        x = int(str(x) + str(y)[0])
        y = int(str(y)[1::])
        for i in range(1, x+1):
            for j in range(1, y+1):
                product = str(i) + str(j) + str(i * j)
                if '0' not in product and len(set(product)) == len(product) == 9:
                    nums.append(i*j)

    return sum(set(nums))


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_32()
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
