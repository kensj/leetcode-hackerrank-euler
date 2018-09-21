import datetime
import timeit

def euler_19(start, end):
    total = 0
    for year in range(start, end):
        for month in range(1, 13):
            if datetime.datetime(year, month, 1).weekday() == 6:
                total += 1
    return total


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_19(1901, 2001)
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
