#https://leetcode.com/problems/implement-strstr/
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle or not haystack:
            # Checks for either parameter to be empty
            return 0
        for i in range(0,len(haystack)-len(needle)):
            # Checks through the array in intervals of up to the length of the needle to see if it is present
            if haystack[i:i+len(needle)] == needle:
                # If match, return i
                return i
        return -1


test = Solution()
print(test.strStr("hello", "ll"))

