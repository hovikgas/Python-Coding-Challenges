'''
From the Codecademy Python track.

Write a function called digit_sum that takes a positive integer n as input 
and returns the sum of all that number's digits.

For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.

Assume that the number you are given will always be positive.
'''

def digit_sum(n):
    num_string = str(n)
    temp = []
    n_sum = 0
    for each in num_string:
        temp.append(int(each))
    for num in temp:
        n_sum += num
    return n_sum
        