'''
Solution by GitHub user @allardbrain in July 2017.

Write a function called no_exponent() that takes in 2 integers, 'num' and 'exp', as arguments.
Both 'num' and 'exp' may be assumed to be positive. Return an integer value of 'num' raised 
to the power of 'exp' without using the exponent operator (**).

>>> no_exponent(5, 3)
125

>>> no_exponent(5, 1)
5

>>> no_exponent(1, 5)
1

>>> no_exponent(0, 3)
0

>>> no_exponent(3, 0)
1

'''


def no_exponent(num, exp):

    value = 1;

    if num == 0:
        return 0

    elif num == 1:
        return num

    else:

        if exp == 0:
            return 1

        elif exp == 1:
            return num

        else:

            for i in range(0, exp):
                value *= num

            return value



no_exponent(7, 3)



if __name__ == '__main__':
    import doctest
    doctest.testmod()