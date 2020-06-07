# https://leetcode.com/problems/longest-common-prefix/
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        # i is used as the current character to compare
        for i in range(0, len(strs[0])):
            for j in range(1, len(strs)):
                # j used as counter for which word in the array is being compared
                if strs[0][i] != strs[j][i]:
                    # Breaks out of the function if the characters do not match
                    return prefix
            prefix = prefix+strs[0][i]


test = Solution()
print(test.longestCommonPrefix(["flower", "flow", "flight"]))