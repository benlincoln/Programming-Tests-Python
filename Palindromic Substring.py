"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    length = len(s)
    longestString = ""
    # Use i in range as opposed to foreach to keep track of index at
    for i in range(0,length - 1):
        if s[i] == s[i+1]:
            currString = s[i] + s[i+1]
            # Prevents out of range
            if i > 0:
                for j in range(1,i+1):
                    # Prevents out of range
                    if (i+1)+j < len(s):
                        if s[i-j] == s[(i+1)+j]:
                            currString = s[i-j] + currString + s[(i+1)+j]
                    else:
                        break
            if len(currString) > len(longestString):
                longestString = currString
    return longestString

print(longestPalindrome("cabbacd"))
