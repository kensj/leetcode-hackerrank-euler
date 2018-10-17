def repeatedString(s, n):
    if n < len(s): return s[0:n].count('a')
    num = s.count('a') * (n//len(s))
    return num + s[0:(n%len(s))].count('a')