'''
From the Codecademy Python track.

Define a function factorial that takes an integer x as input.
Calculate and return the factorial of that number.
'''

def factorial(x):
    product = 1
    while x >= 1:
        product *= x
        x -= 1
    return product