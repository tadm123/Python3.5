# Using Lists

import os

def filling_alph(b1):                     #This function fills up the alphabet list     
        alphabet = [0] * 26                
        for i, char in enumerate(b1):			                 
                index = lookup_dict[char]		                   
                alphabet[index] = alphabet[index] + 1
        return alphabet


def check_match(alph1,alph2):           #checks if all letters of alph1 are in alph2
        for a1, a2 in zip(alph1, alph2):
                if a1 > a2:
                        return False
        return True
                
os.chdir('c:\\users\\patty\\desktop')          
lookup_dict = dict(zip("abcdefghijklmnopqrstuvwxyz", range(26)))  #Creating a lookup table

print('Type a word:')
some_word = input()    
alph1= filling_alph(some_word)
fp = open('allwords.txt')

for line in fp:
	word = line.strip()                   #evaluates each line
	alph2 = filling_alph(word)            #strips new-line characters   
	if check_match(alph1,alph2):                  
		print(word)
		
fp.close()






		
