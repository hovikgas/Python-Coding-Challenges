'''
Write a function 'lucky_sevens(nums)', which takes in a list of integers 
and returns true if any three consecutive elements sum to 7.
Make sure your code currectly checks for the first and last elements of the array.

Test cases:

lucky_sevens?([2,1,5,1,0]) == true # => 1 + 5 + 1 == 7
lucky_sevens?([0,-2,1,8]) == true # => -2 + 1 + 8 == 7
lucky_sevens?([7,7,7,7]) == false
lucky_sevens?([3,4,3,4]) == false
'''

def lucky_sevens(nums):

    for i in range(0, len(nums)):

        if sum(nums[i:i + 3]) == 7:  # i + 3 so that slicing ends after i + 2 (3 consecutive nums)
            print True
            return True   # Inside the loop, because True if ANY 3 consecutive nums sum to 7.

    print False   # outside the loop