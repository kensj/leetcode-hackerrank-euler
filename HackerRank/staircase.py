def staircase(n):
    spaces = n-1
    hashes = 1
    for x in range(0, n):
        print(' ' * spaces + '#' * hashes)
        spaces -= 1
        hashes += 1