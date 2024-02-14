class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # make a new empty arr
        # loop through nums array
            # each iteration
            # check that our new arr does not contain the value 
            # if it doesnt  
                # put it inside the array
            # else 
                # means duplicate and return false
        #
        # return true

        existing_nums = set()
        for num in nums:
            if num in existing_nums:
                return True
            existing_nums.add(num)
        return False