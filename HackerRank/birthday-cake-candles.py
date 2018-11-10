def birthdayCakeCandles(ar):
    occurrences = {}
    tallest = -1
    for a in ar:
        occurrences[a] = occurrences.get(a,0) + 1
        if occurrences[a] > tallest: tallest = occurrences[a]
    return tallest