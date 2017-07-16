'''
Write a function called median that takes a list 
as an input and returns the median value of the list.

For example: median([1,1,2]) should return 1.

The list can be of any size and the numbers are not 
guaranteed to be in any particular order.
If the list contains an even number of elements, 
your function should return the average of the middle two.
'''

def median(num_list):
    
    sorted_list = sorted(num_list)
    print sorted_list
    L = len(sorted_list)
    if L % 2 == 0:
        return (sorted_list[L / 2 - 1] + sorted_list[L / 2]) / 2.0 
    else:   
        return sorted_list[(L / 2)]  
