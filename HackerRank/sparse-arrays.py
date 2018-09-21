def matchingStrings(strings, queries):
    map = {}
    for string in strings:
        if string in queries:
            map[string] = map.get(string, 0) + 1
    
    fin = []
    for query in queries:
        fin.append(map.get(query, 0))
    return fin