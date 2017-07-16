'''
From the Codecademy Python track.

Define a function called is_prime that takes a number x as input.
For each number n from 2 to x - 1, test if x is evenly divisible by n.
If it is, return False.
If none of them are, then return True.
'''

def is_prime(x):
    
    if x < 2:
        return False
        
    for n in range(2, x):
        if x % n == 0:
            return False
            break
    else: return True

            

