'''
Write a function called remove_duplicates() that takes in a list of numbers.
Return a new list that contains only single occurrences of the numbers in the list.
If a number appears more than once, keep the first occurrence but remove any other duplicates.

>>> remove_duplicates([1,1,2,2])
[1, 2]

>>> remove_duplicates([3, 5, 7])
[3, 5, 7]

'''

def remove_duplicates(num_list):

    result = []

    for i in range(len(num_list)):

        if num_list[i] not in result:
            result.append(num_list[i])

    return result


remove_duplicates([2, 4, 6, 2])


if __name__ == '__main__':
    import doctest
    doctest.testmod()