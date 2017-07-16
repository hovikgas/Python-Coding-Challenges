'''
Write a function that takes in an array of integers 
and returns the sum of the odd elements.

Test cases:

oddball_sum([1,2,3,4,5]) == 9 # => 1 + 3 + 5 == 9
oddball_sum([0,6,4,4]) == 0
oddball_sum([1,2,1]) == 2
'''

def oddball_sum(nums):

    i = 0
    result = 0

    for i in range(len(nums)):

        if nums[i] % 2 == 1:
            result += nums[i]

    print result  
    return result


