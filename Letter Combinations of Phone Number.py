# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    strings = []
    # Dictionary containing all the letters corresponding to their numeric counterparts
    dictNumLetters = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'],
                          "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'],
                          "9": ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.cycleThrough("", digits)
        return self.strings

    def cycleThrough(self, currString, nextValues):
            if not nextValues:
                # Checks if anymore characters to account for
                self.strings.append(currString)
            else:
                # Creates a for each loop which in turn performs every possible permutation  
                for char in self.dictNumLetters[nextValues[0]]:
                    self.cycleThrough(currString+char, nextValues[1:])


test = Solution()
print(test.letterCombinations("23"))

