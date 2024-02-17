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

        for i, word in enumerate(strs):    # n
            sub_arr = []
            count = self.generateDict(word)   # k 

            for j, check_word in enumerate(strs):   # n
                check_count = self.generateDict(check_word)  # k
                
                if check_count == count:
                    sub_arr.append(check_word)

            if not sub_arr in result:         # n 
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

# HERE IS THE MOST OPTIMAL SOLUTION
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
