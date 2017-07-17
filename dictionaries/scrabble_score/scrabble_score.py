'''
Write a function called reverse() that takes in a string and returns that string in reverse.

You may not use reversed() or [::-1] to help you with this.
You may get a string containing special characters (for example, !, @, or #).

>>> reverse("Hello!")
'!olleH'

>>> reverse("I love smoothies")
'seihtooms evol I'

'''

def reverse(text):
    
    reversed_str = ""
    
    for i in range((len(text) - 1), -1, -1):
        reversed_str += text[i]

    # print("Original string: ", text)
    # print("Reversed string: ", reversed_str)
    return reversed_str


if __name__ == '__main__':
    import doctest
    doctest.testmod()