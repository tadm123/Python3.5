# Unnecessary censorship program.
# Censors every word that starts with 'f' from your clipboard.

import re,pyperclip

text = str(pyperclip.paste())          

list = split(text)

upRegex= re.compile(r'(f)\w+')

mo= upRegex.sub(r'\1****', text)

pyperclip.copy(mo)



