'''
Solution by GitHub user @allardbrain in July 2017.

Write a function called is_anagram() that takes in 2 strings as arguments.
Return True if the strings are anagrams of each other (ie: they contain the same
letters and no extra letters). Otherwise, return false.

>>> is_anagram("cat", "dog")
False

>>> is_anagram("care", "race")
True

'''

def is_anagram(text1, text2):

    sorted_text1 = sorted(text1)
    sorted_text2 = sorted(text2)
    
    if sorted_text1 == sorted_text2:
        return True
    else:
        return False


is_anagram("blue", "black")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
