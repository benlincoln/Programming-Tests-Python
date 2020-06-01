"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Checks for a match in the intial characters
        intialMatch = s[0] in (p[0], '.')

        if intialMatch and len(s) > 1:
            if p[1] == '*' and s[1] == s[0]:
                # If an asterisk and a repeating char, move s along 1, and p stays the same to compare the current char
                # again
                return self.isMatch(s[1:], p)
            else:
                # For non * chars or a case of the character changing when in a *
                return self.isMatch(s[1:], p[1:]) or self.isMatch(s[1:], p[2:])
        else:
            return intialMatch


test = Solution()
print(test.isMatch("aab", "a*b"))
