import timeit

def euler_7(target):
    current_prime = 0
    count = 0
    current_number = 2
    while count < target:
        # Check if the number if prime
        if is_prime(current_number):
            # Make it the latest prime
            current_prime = current_number
            # Increment our counter
            count += 1
        # Check our next number
        current_number += 1
    return current_prime

def is_prime(current_number):
    for i in range(2,int(current_number ** 0.5)+1):
        if not current_number%i:
            return False
    return True
            
if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_7(10001)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
