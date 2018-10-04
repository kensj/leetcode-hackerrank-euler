class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area, x,y = -1, 0, len(height)-1
        while x<y:
            if height[x]<height[y]:
                total = (y-x)*height[x]
                x += 1
            else:
                total = (y-x)*height[y] 
                y -= 1
            if total > area: area = total
        return area