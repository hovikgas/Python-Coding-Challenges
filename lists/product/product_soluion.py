'''
Define a function called product() that takes a list of integers as input 
and returns the product of all of the elements in the list as an integer.
Assume the list has at least one element in it.

>>> product([5])
5

>>> product([4, 5, 5])
100

'''

def product(integers):

    result = 1

    for i in range(len(integers)):
        result *= integers[i]

    return result


product([3, 4, 5])


if __name__ == '__main__':
    import doctest
    doctest.testmod()