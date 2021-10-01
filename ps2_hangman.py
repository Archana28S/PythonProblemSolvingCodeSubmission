# Problem Set 2
# Name: Archana Sharma
# Time Spent: 3 days



##Problem 4: Implement a function, hangman(), that will start up and carry out an interactive Hangman game between a player and the computer.



import random
# library that we use in order to choose on random words from a list of words.
 
name = input("What is your name ")
# Here the user is asked to enter the name first
 
print("Hello ! ", name)
print("Good Luck....")
 
words = ['ordinary', 'industry', 'nature', 'power','apple', 'metal', 'joy', 'contile','gorgeous', 'waterfall', 'regards', 
        'stale']
                              
word = random.choice(words)
# Function will choose one random word from this list of words.
 
 
print("Guess the letter")
 
guesses = ''
                
turns = 12
# any number of turns can be used here.
 
 
while turns > 0:
# counts the number of times a user fails.
    failed = 0
# all characters from the input word taking one at a time.
    for char in word:
# comparing that character with the character in guesses
        if char in guesses:
            print(char)
             
        else:
            print("_")
# for every failure 1 will be incremented in failure
            failed += 1
             
 
    if failed == 0:
# user will win the game if failure is 0 and 'You Win' will be given as output
        print("You Win!!")
         
# this print the correct word
        print("The word is: ", word)
        break
     
# if user has input the wrong alphabet then it will ask user to enter another alphabet
    guess = input("Guess the letter:")
     
# every input character will be stored in guesses
    guesses += guess
     
# check input with the character in word
    if guess not in word:
         
        turns -= 1
         
# if the character doesn’t match the word then “Wrong” will be given as output
        print("Test")
         
# this will print the number of turns left for the user
        print("You have", + turns, 'more guesses')
         
         
        if turns == 0:
            print("Opps!!You Lose..Better Luck Next Time")


            ##Test Passed
