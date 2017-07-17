'''
Write a function that takes in a string argument, and returns a dictionary containing
the characters in the string, along with the number of times each character appears in the string.
'''

def count_chars(my_string):

    char_count = {}

    for i in range(len(my_string)):

        temp_char = my_string[i]

        if temp_char in char_count:
            char_count[temp_char] += 1

        else:
            char_count[temp_char] = 1


    print("Character counts: ", char_count)
    return char_count;

count_chars("Ahoy! I am a pirate! $ @ 4 5 5 5 { { {");
