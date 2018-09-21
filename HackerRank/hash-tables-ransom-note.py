def checkMagazine(magazine, note):
    table = {}
    for word in magazine:
        table[word] = table.get(word, 0) + 1
    for word in note:
        if table.get(word, 0) is 0:
            print("No")
            return
        table[word] = table[word] - 1
    print("Yes")
