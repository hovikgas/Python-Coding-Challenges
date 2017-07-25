'''
Solution by GitHub user @allardbrain in July 2017.

Write a function called reverse() that takes in a string and returns that string in reverse.

You may not use reversed or [::-1].
You may get a string containing special characters (for example, !, @, or #).

>>> reverse("I love smoothies")
'seihtooms evol I'

>>> reverse("watermelon")
'nolemretaw'

'''

def reverse(text):
    
    reversed_str = ""

    for i in range((len(text) - 1), -1, -1):
        reversed_str += text[i]

    return reversed_str


reverse("Hello, world!")



if __name__ == '__main__':
    import doctest
    doctest.testmod()