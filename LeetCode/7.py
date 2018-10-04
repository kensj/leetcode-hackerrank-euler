class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = [1,-1][x < 0]
        x = s * int(str(abs(x))[::-1])
        return x if (-1*(2**31)-1) < x < ((2**31)) else 0
		