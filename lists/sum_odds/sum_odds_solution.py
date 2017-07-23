'''
Write a function called oddball_sum() that takes in a list of integers 
and returns the sum of the odd elements.

>>> oddball_sum([1,2,3,4,5])
9

>>> oddball_sum([0,6,4,4])
0

>>> oddball_sum([1,2,1])
2

'''

def oddball_sum(nums):

    result = 0

    for i in range(len(nums)):

        if nums[i] % 2 == 1:
            result += nums[i]
 
    return result


oddball_sum([17, 15, 0])


if __name__ == '__main__':
    import doctest
    doctest.testmod()


