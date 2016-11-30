# "Automate the Boring Stuff" Book
# CH7: Find website URLs that begin with http:// or https:// from clipboard

import re, pyperclip

text=str(pyperclip.paste())

phoneRegex = re.compile(r'(http(s)?://\S+)')

mo=phoneRegex.findall(text)

matches =[]

for groups in mo:
	matches.append(groups[0])       #creates a list of urls

if len(matches) > 0:
       pyperclip.copy('\n'.join(matches))   #make it a string
       print('Copied to clipboard: ')
       print('\n'.join(matches))
else:
    print('No urls were found.')
