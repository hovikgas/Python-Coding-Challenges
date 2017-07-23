''' 
Write a function that takes in a list and returns a new, reversed version of the list.
Do not use the list object's .reverse() method.

>>> reverse_array([1, 2, 3, 4, 5])
[5, 4, 3, 2, 1]

>>> reverse_array(['apple', 'boat', 'cat', 'dog'])
['dog', 'cat', 'boat', 'apple']

'''

def reverse_array(my_list):

    reversed_list = [];

    for i in range((len(my_list) - 1), -1, -1):
        reversed_list.append(my_list[i])

    return reversed_list

reverse_array([1, 2, 3, 4, 5]);


if __name__ == '__main__':
    import doctest
    doctest.testmod()
