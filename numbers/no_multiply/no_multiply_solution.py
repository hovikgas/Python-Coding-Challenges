'''
Solution by GitHub user @allardbrain in July 2017.

Write a function called no_multiply() that takes in 2 integers as arguments.
Return the product of these two numbers without using multiplication (the * operator).

>>> no_multiply(3, 5)
15

>>> no_multiply(1, 4)
4


>>> no_multiply(5, 1)
5

>>> no_multiply(0, 9)
0

>>> no_multiply(9,0)
0

'''


def no_multiply(int1, int2):

    result = 0

    for each in range(int2):
        result += int1

    return result


no_multiply(2, 7)


if __name__ == '__main__':
    import doctest
    doctest.testmod()