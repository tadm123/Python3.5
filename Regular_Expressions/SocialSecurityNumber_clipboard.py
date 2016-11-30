# "Automate the boring stuff Book"
# Ch5: Censoring Social security numbers 000-00-0000 , in a text in clipboard

import re, pyperclip

text=str(pyperclip.paste())   

datesRegex= re.compile(r'(\d)\d{2}-\d{2}-\d{4}')

datesstring= datesRegex.sub(r'\1**-**-****', text)

pyperclip.copy(datesstring)
print(datesstring)

