'''
Write a funciton which takes in a string, and returns that string 
with all the vowels removed. Treat "y" as a consonant.

Test cases:

disemvowel("foobar") == "fbr"
disemvowel("ruby") == "rby"
disemvowel("aeiou") == ""

'''

def disemvowel(string):
    
    result = ""

    for i in range(len(string)):

        if string[i] != 'a' and string[i] != 'e' and string[i] != 'i' and string[i] != 'o' and string[i] != 'u':
            result += string[i]

    print result
    return result


disemvowel("appalachia")
