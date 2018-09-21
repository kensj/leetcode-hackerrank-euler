import timeit

to_nineteen = ["one", "two",  "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def euler_17():
    # 1000
    total = len("one") + len("thousand")

    for x in range(0, 9):
        # 100, 200...900
        total += len(to_nineteen[x])
        total += len("hundred")
        # 101-119, 201-219...901-919
        for first in to_nineteen:
            total += len(to_nineteen[x])
            total += len("hundredand")
            total += len(first)
        # 120-190, 120-190...920-990
        for ten in tens:
            total += len(to_nineteen[x])
            total += len("hundredand")
            total += len(ten)
            # 121-199, 121-199...921-999
            for y in range(0, 9):
                total += len(to_nineteen[x])
                total += len("hundredand")
                total += len(ten)
                total += len(to_nineteen[y])


    # 1-19
    total += len(''.join(to_nineteen))
    # 20-90
    total += len(''.join(tens))
    # 21-99
    for ten in tens:
         for y in range(0, 9):
            total += len(ten)
            total += len(to_nineteen[y])

    return total


if __name__== "__main__":
    start = timeit.default_timer()
    ans = euler_17()
    stop = timeit.default_timer()
    print('Answer:', ans)
    print('Runtime:', stop - start)  
