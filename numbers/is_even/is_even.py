'''
Define a function is_even() that will take a number, x, as input.
If x is even, return True. Otherwise, return False.

>>> is_even(6)
True

>>> is_even(5)
False

'''

def is_even(x):

    if x % 2 == 0:
        return True

    else: 
        return False


is_even(10)


if __name__ == '__main__':
    import doctest
    doctest.testmod()