import timeit

def euler_6(target):
    sum_of_square = 0
    square_of_sum = 0
    for i in range(1, target+1):
        # Add to the sum of the squared value
        sum_of_square += i**2
        # Add the sum
        square_of_sum += i
    # get the square of the sum
    square_of_sum **= 2
    # Simple difference
    return square_of_sum - sum_of_square



if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_6(100)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
