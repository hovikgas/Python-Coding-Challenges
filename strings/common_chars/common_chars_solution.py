'''
Write a function called common_chars() that takes in two lowercase strings,
text1 and text2, as arguments. Return a list of the common characters
contained in the two strings.

>>> common_chars("donuts", "tundra")
['d', 'n', 'u', 't']

>>> common_chars("peaches", "door")
[]

'''

def common_chars(text1, text2):

    common_chars = []

    for i in range(len(text1)):

        for j in range(len(text2)):

            if text1[i] == text2[j] and text1[i] not in common_chars:    
                common_chars.append(text1[i])
        
    return common_chars


common_chars("stem", "pick")


if __name__ == '__main__':
    import doctest
    doctest.testmod()