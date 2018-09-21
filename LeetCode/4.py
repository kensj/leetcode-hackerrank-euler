class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newlist = sorted(nums1 + nums2)
        total = len(newlist)
       
        if total%2 == 0:
            return (newlist[total//2-1] + newlist[total//2])/2
        else:
            return newlist[total//2]
            
       