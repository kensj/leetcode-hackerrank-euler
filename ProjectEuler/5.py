import timeit

def euler_5(target):
    total = 1
    # hashmap for global factor usage
    factors_used = {}
    # For each number [1,target]
    for x in range(2, target+1):
        # Get the prime factors
        current_factors = prime_factors(x)
        # each factor in the found prime_factors
        for factor in current_factors:
            # get the count of factor in current_factors
            occurrences = current_factors.count(factor)
            # and the amount of times we used globally
            total_used = factors_used.get(factor, 0)
            # If we have a difference, we can multiply the factor again
            if occurrences > total_used:
                # We will multiply the current total * factor * difference
                difference = occurrences - total_used                
                total *= (factor * difference)
                # We used the remaining difference, so add it to the map
                factors_used[factor] = factors_used.get(factor,0) + difference
    return total

def prime_factors(target):
    # start at 2
    x = 2
    prime_factors = []
    while x <= target:
        # If target is evenly divisible by x
        if not target%x:
            prime_factors.append(x)
            # Divide target by x and check if it's divisible again by x
            target /= x
        else:
            # If it's not divisible by x again, check the next number
            x += 1
    return prime_factors


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_5(20)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
