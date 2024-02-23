# MY SOLUTION SOLVES THE PROBLEM BUT NOT WITHIN THE TIME CONSTRAINT

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        Use two pointers?
        """

        """
        left = 0
        right = length - 1
        have current product equal to arr[left]
        array result

        loop through 

            if left and right are equal
                then skip
            
            we will mutiply the product by arr[right]

            if right = 0
                push product onto result array
                then we reset it to the length - 1
                then we increase left by one 
                product will become the new arr[left]
        """
        
        left = 0
        right = len(nums) - 1
        product = 1
        result = []

        while (len(result) != len(nums)):
            print(product, '<-- product')
            print(left, 'l', right, 'r')
            if (left == right):
                right -= 1

            if (right < 0):
                result.append(product)
                right = len(nums) - 1

                if (len(nums) - 1 == left):
                    continue
                else:
                    left += 1
                
                product = 1
            else:
                product *= nums[right]
                right -= 1

        return result 