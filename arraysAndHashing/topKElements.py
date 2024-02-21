# FIRST RESULT FROM ME, ONLY PASSES SIMPLE TEST CASES

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        have a dict to keep track of all numbers that appear and there count

        loop through num array
            check if it is in dict
                if not 
                    add to, set value to one
                if it is
                    just add one to value
        
        we want to sort these values to get the highest nums in front

        have a list
        then what we want to do is loop up until k
            appending those max values to the list unitl we reach k
        
        return the list
        """

        counts = OrderedDict()

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        result = []
        counter = 0

        for key, value in sorted_counts.items():
            print(key, value)
            if counter == k: 
                break

            result.append(key)
            
            counter += 1
        
        return result