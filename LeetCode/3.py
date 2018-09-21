class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        longest = []
        for x in range(0, len(s)):
            current = {}
            current[s[x]] = 1
            for y in range(x+1, len(s)):
                if current.get(s[y], 0) == 1:
                    longest.append(y-x)
                    break
                else:
                    current[s[y]] = 1
                    if y == len(s)-1:
                        longest.append(y-x+1)
        return max(longest)