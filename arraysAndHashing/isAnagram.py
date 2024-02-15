class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_bank = {}

        for letter in s:
            if letter in letter_bank.keys():
                letter_bank[letter] += 1
            else:
                letter_bank[letter] = 1

        letter_bank_check = {}
        for letter in t:
            if letter in letter_bank_check.keys():
                letter_bank_check[letter] += 1
            else:
                letter_bank_check[letter] = 1

        return letter_bank == letter_bank_check
