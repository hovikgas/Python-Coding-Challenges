'''
Solution by GitHub user @allardbrain in July 2017.

Write a function called reverse() that takes in a string and returns that string in reverse.

You may not use reversed or [::-1].
You may get a string containing special characters (for example, !, @, or #).

>>> reverse_recursion("I love smoothies")
'seihtooms evol I'

>>> reverse_recursion("watermelon")
'nolemretaw'

'''

def reverse_recursion(text):
    
    if len(text) == 0:
        return "You can't reverse an empty string!"

    if len(text) == 1:
        return text
        
    if len(text) > 1:

        # Return last char in string, slice it off, repeat until all chars returned
        return text[-1] + reverse_recursion(text[:-1]) 


reverse_recursion("Hello, world!")



if __name__ == '__main__':
    import doctest
    doctest.testmod()