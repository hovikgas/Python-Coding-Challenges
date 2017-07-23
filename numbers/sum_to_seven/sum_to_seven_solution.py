'''
Write a function  called lucky_sevens(nums) which takes in a list of integers 
and returns true if any three consecutive elements sum to 7.

Test cases:

>>> lucky_sevens([2,1,5,1,0])
True

>>> lucky_sevens([0,-2,1,8])
True

>>> lucky_sevens([7,7,7,7])
False

>>> lucky_sevens([3,4,3,4])
False
'''

def lucky_sevens(nums):

    for i in range(len(nums) - 2):

        # i + 3 so that slicing ends after i + 2 (3 consecutive nums)
        if sum(nums[i:i + 3]) == 7:  
            return True

    return False


lucky_sevens([5, 3, 2, 2])


if __name__ == '__main__':
    import doctest
    doctest.testmod()