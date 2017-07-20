'''
Write a function called median() that takes a list of numbers 
as an argument and returns the median value of the list.

The median value is determined by choosing the middle number in a sorted list.
If the list contains an even number of items, the median is the average of the middle two.

>>> median([1,1,2]) 
1

>>> median([1, 2, 3, 4])
2.5

'''

def median(num_list):
    
    sorted_list = sorted(num_list)
    length_sorted_list = len(sorted_list)

    if length_sorted_list % 2 == 0:

        # Use // for division or else you get an error for indexing a float
        # See: https://stackoverflow.com/questions/1282945/python-integer-division-yields-float
        return (sorted_list[(length_sorted_list // 2) - 1] + sorted_list[length_sorted_list // 2]) / 2 
    
    else:   
        return sorted_list[(length_sorted_list // 2)]  


median([5, 6, 7])



if __name__ == '__main__':
    import doctest
    doctest.testmod()