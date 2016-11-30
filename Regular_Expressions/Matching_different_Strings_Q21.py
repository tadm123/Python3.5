# "Automate the boring stuff" Book
# CH7: Exercise Q.21

import re

def testing(text):
    Regex= re.compile(r'^[A-Z][a-z]+\s(Nakamoto)')
    mo=Regex.search(text)
    if mo == None:
        print('Error')
    else:
        print(mo.group())


text = ['Satoshi Nakamoto','Alice Nakamoto', 'Robocop Nakamoto',
       'satoshi Nakamoto', 'Mr.Nakamoto', 'Nakamoto','Satoshi nakamoto']


for i in range(len(text)):
    testing(text[i])

