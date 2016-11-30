# "Automate The Boring Stuff" Book
#  CH 3 Project: guessThatNumber.py

#  This is a guess the number game.

import random
secretNumber= random.randint(1,20)
print('I am thinking of a number between 1 and 20')

#Ask the player to guess 6 times
for guessesTaken in range(1,7):      #notice that after 6 tries it goes out of the for loop
    print('Take a guess.')
    guess=int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    #This condition is the correct guess
                 
if guess == secretNumber:
    print('Good job! You guessed my number in ' +str(guessesTaken)+' guesses!')
else:
    print('Nope. The number I was thinking is ' + str(secretNumber)+ '..')
