class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
    
        string = ""
        length = 0
        for x in range(1, len(s)-1):
            middle1 = -1
            middle2 = -1

            if s[x] == s[x+1]:
                middle1 = x
                middle2 = x+1
                while middle1 > -1 and middle2 < len(s) and s[middle1] == s[middle2]:
                    middle1 -= 1
                    middle2 += 1
                middle1 += 1
                tlen = len(s[middle1:middle2])
                if tlen > length and middle1 > -1 and middle2 > -1:
                    string = s[middle1:middle2]
                    length = len(string)
                    
            if s[x-1] == s[x]:
                middle1 = x-1
                middle2 = x
                while middle1 > -1 and middle2 < len(s) and s[middle1] == s[middle2]:
                    middle1 -= 1
                    middle2 += 1
                middle1 += 1
                tlen = len(s[middle1:middle2])
                if tlen > length and middle1 > -1 and middle2 > -1:
                    string = s[middle1:middle2]
                    length = len(string)

            if s[x-1] == s[x+1]:
                middle1 = x-1
                middle2 = x+1
                while middle1 > -1 and middle2 < len(s) and s[middle1] == s[middle2]:
                    middle1 -= 1
                    middle2 += 1
                middle1 += 1
                tlen = len(s[middle1:middle2])
                if tlen > length and middle1 > -1 and middle2 > -1:
                    string = s[middle1:middle2]
                    length = len(string)

        if not length:
            return s[0]
        return string
