'''
Solution by GitHub user @allardbrain in July 2017.

Define a function called is_prime() that takes a number, x, as input.
For each number n from 2 to x - 1, test if x is evenly divisible by n.
If x is evenly divisible by n, return False, since prime numbers are 
only divisible by themselves and 1. If x is not evenly divisible by n, 
then return True, since prime numbers are not divisible by anything but 
themselves and 1.

>>> is_prime(27)
False

>>> is_prime(5)
True

'''

def is_prime(x):
    
    if x < 2:
        return False
        
    for n in range(2, x - 1):
        if x % n == 0:
            return False

    return True

is_prime(3)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
            

