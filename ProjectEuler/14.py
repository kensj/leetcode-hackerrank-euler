import timeit

#sequence_length = {}

def euler_14(ceil):
    largest = 0
    starting = 0
    for x in range(1, ceil+1):
        # Get the sequence
        current = sequence_list(x)
        # Save the largest chain and its starting number
        if current > largest:
            largest = current
            starting = x
    return starting
    

def sequence_list(n):
    # Start with size 1 (just element n)
    length = 1
    while n != 1:
        # If the n exists, we will save it to the map for future use
        #if sequence_length.get(n, 0):
            #return length + sequence_length[n]
        # perform necessary conversion based on value
        if not n%2:
            n = int(n/2)
        else:
            n = int(n*3 + 1)
        length += 1
    # Save the sequence length for future use
    # sequence_length[n] = length
    return length

if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_14(1000000)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
