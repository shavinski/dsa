class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # we want a dict to store
        # key as index of number
        # value will be the number itself

        # we will want to loop through array
        # check if the current number and index exists in dict
        # if not we will add it

        # next we will see if the current num will add up with prev num to equal target
        # if thats the case then return list of the indexs of nums

        num_dict = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in num_dict:
                return [num_dict[difference], i]

            num_dict[num] = i

        return []
    
    # [1,2,3,4] target = 5

    # begin iteration i = 0
    # checks if 
    #     5 - 1 = 4 is in dict
    #     current dict is {}
    #     its not 
    
    # so adds it at end
    #     current dict is {1:0}

    # next iteration  i = 2
    # checks if 
        #     5 - 2 = 3 is in dict
        #     current dict is {1:0}
        #     its not 
        
        # so adds it at end
        #     current dict is {1:0, 2:1}
    
    # next iteration i = 2
    # checks if 
        #     5 - 3 = 2 is in dict
        #     current dict is {1:0, 2:1}
        #     it is !
    
        #  so now we return a list
            #  the list will return the index which 2 exists at and the current index
            #  return [dict[target - current_num],i]
            # dict[target] = dict[2] = 1
            # so return [1,2]
        