'''
Define a function called count() that has two arguments, called sequence (a list) and item.
The item you input may be an integer, string or float.
Return an integer representing the number of times the item occurs in the sequence.

>>> count([1, 4, 1, 3, 1, 6], 1)
3

>>> count(["boat", "kayak", 1, 3, "boat"], "boat")
2
'''
def count(sequence, item):
    
    result = 0
        
    for i in sequence:
        if i == item:
            result += 1

    return result


count(["hello", "poodle", "chocolate"], "chocolate")


if __name__ == '__main__':
    import doctest
    doctest.testmod()