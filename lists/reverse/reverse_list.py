''' Write a function that takes in a list and returns a new, reversed version of the list.
Do not use the list object's .reverse() method.
'''

def reverse_array(my_list):

    reversed_list = [];

    for i in range((len(my_list) - 1), -1, -1):
        reversed_list.append(my_list[i])

    print("Original list: ", my_list)
    print("Reversed list: ", reversed_list)
    return reversed_list

reverse_array([1, 2, 3, 4, 5]);
