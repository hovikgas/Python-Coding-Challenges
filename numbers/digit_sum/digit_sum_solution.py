'''
Solution by GitHub user @allardbrain in July 2017.

Write a function called digit_sum() that takes a positive integer n as input 
and returns the sum of all that number's digits.

>>> digit_sum(1234)
10

>>> digit_sum(10)
1

>>> digit_sum(5)
5

'''

def digit_sum(n):

    num_string = str(n)
    n_sum = 0

    for each in num_string:
        n_sum += int(each)

    return n_sum


digit_sum(1234)


if __name__ == '__main__':
    import doctest
    doctest.testmod()