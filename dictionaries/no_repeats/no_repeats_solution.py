'''
Write a function called no_repeats() that takes in a string argument
and returns the first character in the string that does not have a 
duplicate elsewhere in the string. Assume there are only letters in 
the input string. Letters should count as duplicates regardless of 
capitalization.

>>> no_repeats("")
'No characters in an empty string.'

>>> no_repeats("t")
't'

>>> no_repeats("tt")
'No unique characters found.'

>>> no_repeats("tth")
'h'

>>> no_repeats("Do not go quietly into that dark night")
'q'

'''

def no_repeats(text):

    text = text.lower()
    char_counts = {}

    if text == "":
        return "No characters in an empty string."
    
    # First loop through 'text' sets up dictionary
    for char in text:

        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    
    # Second loop through 'text' finds first char with only one occurrence
    for char in text:

        if char_counts[char] == 1:
            return char

    return "No unique characters found."


no_repeats("Four score and seven years ago")


if __name__ == '__main__':
    import doctest
    doctest.testmod()