'''
Write a function called disemvowel() which takes in a string, and returns that string 
with all the vowels removed. Treat "y" as a consonant.

>>> disemvowel("foobar")
'fbr'

>>> disemvowel("ruby")
'rby'

>>> disemvowel("aeiou")
''

'''

def disemvowel(text):
    
    result = ""
    vowels = "aeiouAEIOU"

    for i in range(len(text)):

        if text[i] not in vowels:
            result += text[i]

    # print result
    return result


disemvowel("appalachia")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
