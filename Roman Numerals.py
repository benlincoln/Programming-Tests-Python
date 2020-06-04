# https://leetcode.com/problems/roman-to-integer/
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = None
        summation = 0
        # Dictionary for values
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for index, char in enumerate(s, 0):
            # Uses enumerate so can use a for each whilst keeping track of index
            if index > 0:
                # A the value of the numeral is deducted from the next value if it is lower than previous, I test this
                # using a temp value to compare to, as there is no numeral for 0, I use that as a place holder to
                # indicate when it has been reset
                if temp < values[char] and temp != 0:
                    summation += values[char] - temp
                    temp = 0
                    # I then  continue to ensure that the value of the current character is not assigned to temp
                    continue
                else:
                    # Adds the temp value if no subtraction required
                    summation += temp
            temp = values[char]
        return  summation

test = Solution()
print(test.romanToInt("MCMXCIV"))
