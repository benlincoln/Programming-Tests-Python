"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        currString = ""
        # Loops through each character
        for char in s:
            # Checks if already present
            if char in currString:
                # Gets the longest string out of current string and longest, setting whichever is longest
                if len(currString) > len(longest):
                    longest = currString
                # Resets current string
                currString= char
            else:
                # Appends to current string if not already in the string
                currString = currString+char
        print(longest)
        print (len(longest))
        return len(longest)


