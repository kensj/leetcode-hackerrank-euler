def twoStrings(s1, s2):
    letters = {}
    for letter in s1:
        letters[letter] = 1
    for letter in s2:
        if letters.get(letter, 0) is 1:
            return "YES"
    return "NO"
	