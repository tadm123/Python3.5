# "Automate the boring stuff" Book
# CH7: Exercise Q.22

import re

def testing(text):
    Regex= re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.',re.I)
    mo=Regex.search(text)
    if mo == None:
        print('Error')
    else:
        print(mo.group())


text = ['Alice eats apples.','Bob pets cats', 'Carol throws baseballs.',
       'Alice throws Apples.', 'BOB EATS CATS.', 'Robocot eats apples.',
        'ALICE THROWS FOOTBALLS.', 'Carol eaats 7 cats.']

i=0
for i in range(len(text)):
    testing(text[i])

