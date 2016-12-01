# This program finds if a word is a Palindrome.

import re

try:
    while True:
            word = input('Type a word:\n')
            regex= re.compile('[a-zA-Z0-9]+').findall(word)
            word= ''.join(regex).lower()
            print('%s' %('Palindrome' if word == word[::-1] else 'Not Palindrome'))
except KeyboardInterrupt:
            print('Done.')

        
        

