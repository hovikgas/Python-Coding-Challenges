'''
Solution by GitHub user @allardbrain in July 2017.

Write a function called only_letters() that takes in a string of words separated by spaces.
Assume the words have both lower- and uppercase letters, numbers and punctuation in them. 
Strip out all nonalphabetic characters, then sort the words in alphabetical order (ignore 
capitalization) and return the first word. 

>>> only_letters("c$c. %ba! bb#?")
'ba'

>>> only_letters("M3ery&&l St%r3e3ep i#s aw4eso0me?!")
'awesome'

'''

import re

def only_letters(text):

    lower_case = re.compile('^[a-z]$')

    word_list = text.split(' ')
    gather_word_letters = []
    final_word_list = []

    # Remove non-alphabetic characters
    for word in word_list:

        for char in word:

            match = lower_case.match(char)

            if match:
                gather_word_letters.append(char)

        final_word_list.append(gather_word_letters)
        gather_word_letters = []

    # Sort the list of alpha-only words and return the first word
    sorted_final_word_list = sorted(final_word_list)
    first_word = "".join(sorted_final_word_list[0])

    return first_word


only_letters("c$c. %ba! bb#?")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

