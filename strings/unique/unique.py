'''
Write a function called check_unique() that takes in a string argument called 'text'
and returns True if each character in the string argument is unique and False if there
are character duplicates.

>>> check_unique("donuts")
True

>>> check_unique("summer")
False

'''

def check_unique(text):

    unique_chars = []
    
    for char in text:

        if char in unique_chars:
            return False
        else:
            unique_chars.append(char)

    return True


check_unique("unicorn")


if __name__ == '__main__':
    import doctest
    doctest.testmod()