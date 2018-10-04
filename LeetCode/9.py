class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: return False
        x = str(x)
        if len(x) < 2: return True
        a,b = 0,len(x)-1
        while a<b:
            if x[a] != x[b]: return False
            a += 1
            b -= 1
        return True
