"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Below would be the simple way to do it in Python using sort
        jointNums = nums1+nums2
        jointNums.sort()
        length = len(jointNums)
        length -= 1
        mid = length/2
        # Calculate mean differently based upon whether length of new array is even or odd
        if length % 2 == 1:
            # For even length arrays, the mid value contain a half, thus take the index above and below and get the mid
            result = (jointNums[mid-0.5] + jointNums[mid+0.5]) / 2
        else:
            # Odd length arrays
            result = jointNums[mid]
        return result


