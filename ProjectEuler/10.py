import timeit

def euler_10(n):
    total = 0
    current_number = 2
    # Current_number to check if prime
    while current_number < n:
        is_prime = True
        # Check through the factors
        for i in range(2,int(current_number ** 0.5)+1):
            if (current_number % i) == 0:
                is_prime = False
                break
        # If it is prime, add to the total
        if is_prime:
            total += current_number
        # Check next number
        current_number += 1
    return total


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_10(2000000)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runt ime:', stop - start)  
