# hangman.py
# This program is a game of hangman, you can choose to guess either countries or capitals.

import requests, bs4, sys
from random import randint

hangman='''
     _____________    
    |/            |   
    |                 
    |               
    |                 
    |                 
   ---
'''


def all_indexes(letter,word):
        b=[]
        for i,j in enumerate(word):
                if letter == j:
                        b.append(i)
        return b

def stick_figure(strikes):
	if strikes == 1:
		return '    |             O '
	elif strikes == 2:
		return '    |             | '
	elif strikes == 3:
		return '    |            -| '
	elif strikes == 4:
		return '    |            -|-'
	elif strikes == 5:
		return '    |            /  '
	elif strikes == 6:
		return '    |            / \ '

print('\t\t~~~~~~~~~~ Hangman Game ~~~~~~~~~~~~')
for i in hangman.splitlines():
	print(i)
res = requests.get('https://en.wikipedia.org/wiki/List_of_national_capitals_in_alphabetical_order')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text , "html.parser")

print('''Type 'con' for Contries and 'cap' for Capitals: ''')
select = input()

if select == 'cap':
        Elem = soup.select('table.wikitable.sortable tr td a[title]')
elif select == 'con':
        Elem = soup.select('table.wikitable.sortable tr td b a[title]')
else:
        print('Please select a valid option')
        sys.exit()
        
capitals = []
for i in range(len(Elem)):
	capitals.append(Elem[i].get('title'))

rand_capital= capitals[randint(0,len(capitals))].lower()    #producing a random capital

a=[]
strikes =0
lookup_table = '344455'                  #pattern to call stick_figure() in order to print the body of hangman
hangman = hangman.splitlines()

for i in range(len(rand_capital)):
        a.append('_') if rand_capital[i].isalpha() else a.append(rand_capital[i])
        
print('\n')

while strikes< 6:
        print(' '.join(a))
        print('Type a letter:')
        letter = input()
        index= all_indexes(letter,rand_capital)  #find the indexes of rand_capital where this letter appears
        if not index:              #if the index list is empty (no matches)
                strikes += 1
                print('strikes: %d' %strikes)
                hangman[int(lookup_table[strikes-1])]= stick_figure(strikes)
        for line in hangman:            #printing the hangman
                print(line)
        for i in range(len(index)):
                a[index[i]] = letter
        if '_' not in a:
                print(' '.join(a))
                print('You won. The man was saved!.')
                sys.exit()

print('The man has been hanged.')
print('The %s was: %s' %('Capital' if select=='cap' else 'Country',rand_capital.title()))
              

