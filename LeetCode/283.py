class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for x in range (0, len(nums)-1):  
            if nums[x] == 0:
                for y in range(x+1, len(nums)):
                    if nums[y] != 0:
                        nums[x], nums[y] = nums[y], nums[x] 
                        break
