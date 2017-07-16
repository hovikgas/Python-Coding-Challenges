'''
From the Codecademy Python track.

Define a function called reverse that takes a string text and returns that string in reverse.

For example: reverse("abcd") should return "dcba".

You may not use reversed or [::-1] to help you with this.
You may get a string containing special characters (for example, !, @, or #).
'''

def reverse(text):
    
    reversed_str = ""
    index = -1
    
    while abs(index) <= len(text):
        reversed_str = reversed_str + text[index]
        index -= 1
    return reversed_str