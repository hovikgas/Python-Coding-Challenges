'''
Define a function factorial() that takes an integer x as input
and returns the factorial of x. A factorial of a number is 
calculated as a number multiplied by all the numbers that are 
less than it. Example:

5! = 5 * 4 * 3 * 2 * 1

1! and 0! should both return 1.

>>> factorial(5)
120

>>> factorial(0)
1

>>> factorial(1)
1

'''

def factorial(x):

    product = 1

    if x == 1 or x == 0:
        return product

    while x > 1:
        product *= x
        x -= 1

    return product


factorial(3)


if __name__ == '__main__':
    import doctest
    doctest.testmod()