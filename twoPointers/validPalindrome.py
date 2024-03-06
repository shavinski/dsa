class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = ''

        for char in s:
            if char.isalnum():
                result += char.lower()
        
        return result == result[::-1]