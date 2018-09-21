class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_map = {}
        for n in nums:
            n_map[n] = n_map.get(n, 0) + 1
        
        for key in n_map:
            if n_map[key] == 1:
                return key