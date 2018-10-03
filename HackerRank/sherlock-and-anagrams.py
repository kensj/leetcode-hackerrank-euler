def sherlockAndAnagrams(s):
    pairs = {}
    count = 0
    for x in range(0, len(s)):
        for y in range(x+1, len(s)+1):
            string = ''.join(sorted(s[x:y]))
            if len(string): 
                pairs[string] = pairs.get(string,0) + 1
                if pairs.get(string,0) == 2: count += 1
                elif pairs.get(string,0) > 2:
                    count -= ((pairs[string]-2)*(pairs[string]-1))//2
                    count += ((pairs[string]-1)*(pairs[string]))//2
    return count
