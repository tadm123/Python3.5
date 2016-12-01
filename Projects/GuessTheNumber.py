# Guess that number game

import sys
from random import randint

count=0
ranNum = randint(1,20)

list=['Four','Three','Two','One','Zero']

print('******* Guess a number between 1 and 20. You have 5 tries *****\n\n')

while count < 5:
    guess = int(input('Guess a number: '))
    count=count+1
    if guess<ranNum:
        print('\t\t**** Too low! ',end='')       
    elif guess>ranNum:
        print('\t\t**** Too high! ',end='')        
    elif guess == ranNum:
        print('\nYou got it! You solved it in %s %s.'
              %(str(count),'try' if count==1 else 'tries'))
        sys.exit()
    print('%s tries left. ****' %list[count-1])

print('Game over.')

    
