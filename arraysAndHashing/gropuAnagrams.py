# FIRST SOLUTION TERRIBLE TIME COMPLEXITY BUT IT PASSES BASE TEST CASES

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        """
        result arr

        Start loop, get first word
            empty arr
            helper function, creates a dict with letters count

                for loop
                    helper function creates a dict

                    if the word is the same
                        then skip
                    check dict == dict
                        if it is put in arr
        """
        result = []

        for i, word in enumerate(strs):
            sub_arr = []
            count = self.generateDict(word)

            for j, check_word in enumerate(strs):
                check_count = self.generateDict(check_word)
                
                print('count', count, 'check', check_count, check_count == count)

                if check_count == count:
                    sub_arr.append(check_word)

            if not self.isInArray(result, sub_arr):
                result.append(sub_arr)
            
        
        return result
    
    def generateDict(self, word):
        letter_count = {}

        for char in word:
            if char not in letter_count:
                letter_count[char] = 1
            else:
                letter_count[char] += 1

        return letter_count
    
    def isInArray(self, arr, sub_arr):
        for a in arr:
            if a == sub_arr:
                return True
        
        return False

