# Taken from https://leetcode.com/problems/container-with-most-water/
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution(object):
    def maxAreaONSquared(self, height):
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

# Better method using a head and tail, thus allowing for O(n) as opposed to O(n^2)
    def maxAreaON(self, height):
        tail = len(height)-1
        maxVal = 0
        for head in range(0,len(height)):
            if head < tail:
                x = tail - head
                y = min(height[head], height[tail])
                curr = x*y
            else:
                return maxVal
            maxVal = max(maxVal, curr)

test = Solution()
print(str(test.maxAreaONSquared([1,8,6,2,5,4,8,3,7])))
print(str(test.maxAreaON([1,8,6,2,5,4,8,3,7])))