'''
From the Codecademy Python track

Write a function remove_duplicates that takes in a list 
and removes elements of the list that are the same.

For example: remove_duplicates([1,1,2,2]) should return [1,2].

Don't remove every occurrence, since you need to keep a single occurrence of a number.
The order in which you present your output does not matter. So returning [1,2,3] is the same as returning [3,1,2].
Do not modify the list you take as input! Instead, return a new list.
'''

def remove_duplicates(num_list):
    result = []
    for i in range(len(num_list)):
        if num_list[i] not in result:
            result.append(num_list[i])
    return result