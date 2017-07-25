'''
Solution by GitHub user @allardbrain in July 2017.

Define a function is_int() that takes a number, x, as an input.
Have it return True if the number is an integer (as defined below) and False otherwise.

An integer is just a whole number, meaning a number without a decimal.
For instance, -17, 0, and 42 are all integers, but 98.6 is not.

>>> is_int(0)
True

>>> is_int(1)
True

>>> is_int(100)
True

>>> is_int(95.7)
False

'''

def is_int(x):

    if x == 0:
        return True

    elif x / round(x) == 1:
        return True

    else:
        return False


is_int(27)


if __name__ == '__main__':
    import doctest
    doctest.testmod()