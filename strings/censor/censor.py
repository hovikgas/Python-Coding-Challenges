'''
From the Codecademy Python track.

Write a function called censor that takes two strings, text and word, as input. 
It should return the text with the word you chose replaced with asterisks. 
Assume your input strings won't contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in the censored word.
'''

def censor(text, word):
    
    stars = "*" * len(word)
    split_words = text.split()
    
    for each in split_words:
        if each == word:
            split_words[split_words.index(each)] = stars
            
    censored_text = " ".join(split_words)
    return censored_text

            
