''' Write a function that asks a user to guess the value of a random number.
If they guess a number that is too low, tell them so, and prompt them to try again.
If they guess a number that is too high, tell them so, and prompt them to try again.
If they guess a number they have already guessed, tell them so, and prompt them to try again.
If they guess correctly, tell them so, and also tell them how many tries it took.
'''

import random

num = random.randint(1,100)
tries = 0
guessList = []

def guess_number():

    guess = input("The computer is thinking of a number between 1 and 100. Enter your guess here: ")
    guessList.append(guess)

    while tries < 100:

        if guessList.count(guess) >= 2:
            guess = input("Whoops, you already guessed that number! Guess again: ")
            tries += 1

        if guess < num:
            guess = input("Darn, too low. Guess again: ")
            guessList.append(guess)
            tries += 1

        if guess > num:
            guess = input("Shucks, too high. Guess again: ")
            guessList.append(guess)
            tries += 1

        if guess == num: 
            uniqueTries = str(len(set(guessList)))        
            print ("Congratulations, you got it in " + uniqueTries + " unique guesses!")
            tries += 1

    
    
