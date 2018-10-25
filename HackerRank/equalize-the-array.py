def equalizeArray(arr):
    total_count = 0
    max_occurrences = -1
    occurrences = {}
    for a in arr:
        total_count += 1
        occurrences[a] = occurrences.get(a,0) + 1
        if occurrences[a] > max_occurrences: max_occurrences = occurrences[a]
    return total_count - max_occurrences
