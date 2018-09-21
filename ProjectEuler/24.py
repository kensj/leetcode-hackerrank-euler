from itertools import permutations
import timeit

def euler_24(n):
    string = ""
    targets = get_perms(9)[n-1]

    for target in targets:
        string += str(target)
        
    return string

def get_perms(n):
    return(sorted(list(permutations(range(0, n+1)))))

if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_24(1000000)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
