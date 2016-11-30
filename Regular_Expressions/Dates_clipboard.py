# The "Automate The Boring Stuff" Book
# CH 5: Tic-Tac-Toe Board.
# Clean up dates in different date formats (such as 3/14/2015, 03-14-2015, and 2015/3/14)
# by replacing them with dates in a single, standard format.

import re, pyperclip

text=str(pyperclip.paste())

datesRegex= re.compile(r'((\d+)[/-](\d+)[/-](\d+))')

mo=datesRegex.findall(text)

matches =[]

for groups in mo:
        if len(groups[1])> len(groups[3]):
                datesstring= '/'.join([groups[3],groups[2],groups[1]])
        else:
                datesstring= '/'.join([groups[1],groups[2],groups[3]])    

        matches.append('• ' + datesstring)        #creates a list of dates in 'match' list

                
if len(matches) > 0:      
       pyperclip.copy('\n'.join(matches))   #make it a string
       print('Copied to clipboard: ')
       print('\n'.join(matches))
else:
    print('No dates were found.')


'''
Copied to clipboard: 
22/04/1996
22/04/96
04/22/96
'''
