'''
Solution by GitHub user @allardbrain in July 2017.

Define a function called purify that takes in a list of numbers. 
Return a new list that contains only the even numbers from the input list.
Assume zero is an even number.

>>> purify([1,2,3])
[2]

>>> purify([0, 100, 101, 201])
[0, 100]

'''

def purify(numbers):

    result = []

    for i in range(len(numbers)):

        if numbers[i] % 2 == 0:
            result.append(numbers[i])

    return result


purify([5, 10, 15, 20, 25, 30])


if __name__ == '__main__':
    import doctest
    doctest.testmod()