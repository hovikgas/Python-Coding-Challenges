'''
From the Codecademy Python track.

An integer is just a number without a decimal part 
For instance, -17, 0, and 42 are all integers, but 98.6 is not.

For the purpose of this lesson, we'll also say that a number with a decimal part
that is all 0s is also an integer, such as 7.0.

This means that, for this lesson, you can't just test the input 
to see if it's of type int.

If the difference between a number and that same number rounded down 
is greater than zero, what does that say about that particular number?

Define a function is_int that takes a number x as an input.
Have it return True if the number is an integer (as defined above) and False otherwise.
'''

def is_int(x):
    if x == 0:
        return True
    if x / round(x) == 1:
        return True
    else:
        return False