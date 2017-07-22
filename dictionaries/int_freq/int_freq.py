'''
Write a function called int_frequency() that takes a list of positive integers as
an argument and returns the integer that appears the most frequently in the list.
If there are multiple integers that share the same high frequency, return any one
of the integers. If the list is empty, return None.

>>> int_frequency([])


>>> int_frequency([3, 3, 4, 4, 5, 5]) == 3 or 4 or 5
True

>>> int_frequency([1, 1, 3, 2, 1, 4, 3, 5])
1

'''

def int_frequency(intlist):    

    int_freq_dict = {}

    # If inlist is not empty (ie: if it is True)
    if intlist:

        for i in range(len(intlist)):

            if intlist[i] not in int_freq_dict:
                int_freq_dict[intlist[i]] = 1

            else:
                int_freq_dict[intlist[i]] += 1

        # .items() returns a list of tuples containg all (key, value) pairs
        freq_data = int_freq_dict.items()
        
        temp_freq = 0
        temp_num = 0

        for pair in freq_data:

            if pair[1] > temp_freq:
                temp_freq = pair[1]
                temp_num = pair[0]

        return temp_num

    # If intlist is empty
    else:
        return None


int_frequency([3, 3, 4, 4, 5, 5])


if __name__ == '__main__':
    import doctest
    doctest.testmod()


