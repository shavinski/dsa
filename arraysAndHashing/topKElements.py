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
    
# SOLUTION THAT PASSES ALL CASES 
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

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Creates count dictionary, counts each number on how many times it is in array
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Creates frequency array of how many times a number shows up
        # The number of times a num shows up is tied to the index in this array
        # ex:
            """
                 0   1   2   3   4   5   6
                [[], [], [], [], [], [], []]

                [1, 1, 1, 2, 2, 3]

                One shows up three times
                Two shows up two times
                Three shows up once
                
                  0   1    2    3   4   5   6
                [[], [3], [2], [1], [], [], []]

                This is the same size as the length of nums, a number can possibly 
                show up six times, hence why we need the length
            """
        for key, val in count.items():
            freq[val].append(key)


        """
            Now we will loop backwards in the freq array

              0    1    2    3   4   5   6
             [[], [3], [2], [1], [], [], []]

             We loop through starting with six
             Then go down to 3
                then we append the number in the "third" array
            
            so result = [1]

            then the same repeats 
            go down to 2
            the 2 is in there and we append

            so result = [1,2]
            and now we met our k length requirement 
            and now return 

        """
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                
                if len(result) == k:
                    return result