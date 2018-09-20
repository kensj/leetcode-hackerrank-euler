import timeit

def euler_4():
    largest = -1
    # Start from largest 3-digit number
    for i in range(999, 99, -1):
        find = False
        # And check that with the next largest 3-digit number
        for j in range(999, 99, -1):
            num = i * j
            if str(num) == str(num)[::-1] and num > largest:
                # Save the largest palindrome
                largest = num
    return largest


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_4()
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runt ime:', stop - start)  
