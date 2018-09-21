class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = {}
        for letter in J:
            jewels[letter] = 1
            
        total = 0
        for letter in S:
            if jewels.get(letter, 0) > 0:
                total += 1
                
        return total