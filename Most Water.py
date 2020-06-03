# Taken from https://leetcode.com/problems/container-with-most-water/
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # To store indexes
        currentMax = 0
        for i in range(0, len(height)):
            if i > 0:
                for j in range(0, i):
                    # Gets difference in x and y
                    x = (i - j)
                    # Gets height based on 
                    y = min(height[i], height[j])
                    currentMax = max(x*y, currentMax)
        return currentMax


test = Solution()
print(str(test.maxArea([1,8,6,2,5,4,8,3,7])))