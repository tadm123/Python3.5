# "Automate the Boring Stuff" Book  
# CH 7: Strong Password Detection Project
# Test if your password is strong. A strong password is defined as one that
# is at least eight characters long, contains both uppercase and lowercase characters,
# and has at least one digit.

import re

def testing(text): 
    reg8= re.compile(r'\w{8}')
    reglow= re.compile(r'[a-z]')
    regup= re.compile(r'[A-Z]')
    regdig= re.compile('\d')

    if reg8.search(text) != None and reglow.search(text) != None and regup.search(text) != None and regdig.search(text) != None:
            print('Strong password')
    else:
            print('Invalid password')
    
while True:
    print('Enter your password: ',end='')
    password = input()                  
    testing(password)


