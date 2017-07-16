'''
From the Codecademy Python track. 

Define a function called count that has two arguments called sequence and item.
Return the number of times the item occurs in the list.
For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).
Your function should return an integer.
The item you input may be an integer, string, float, or even another list!
'''
def count(sequence, item):
    result = 0
    for i in sequence:
        if i == item:
            result += 1
    return result