# "Automate the boring Stuff" Book
# CH8: mcb.pyw - Saves and loads pieces of text to the clipboard. (mcb= multiclipboard)

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       py.exe mcb.pyw list - Loads all keywords to clipboard.
#       py.exe mcb.pyw delete <keyword> - Deletes a keyword from the shelf.
#       py.exe mcb.pyw delete - Deletes all keywords from shelf.

import shelve, pyperclip, sys

mcbShelf= shelve.open('c:\\users\\patty\\desktop\\loops\\python_command\\mcb')

#Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':        #argc or len(sys.argv)-> 1 location, 2-> save, 3->keyword
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':   # Deletes a keyword from the shelf
        if sys.argv[2] in mcbShelf:         #if the keyword is in mcbShelf
            del mcbShelf[sys.argv[2]]
        else:
            print('Keyword not found')

elif len(sys.argv) == 2:

#List keywrods and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        mcbShelf.clear()                         #deletes whole dictionary 

mcbShelf.close()
   

#to delete a dictionary item use: del name['Daniel']
#to delete the whole dictionary items: del name

#ex:
'''
(clipboard: 'Write a program that opens all')

py.exe mcb.pyw save test1

(clipboard: '2222222222222222')

py.exe mcb.pyw save test2

(clipboard: 'HELLO MY FRIENDASDF')

py.exe mcb.pyw save test3


py.exe mcb.pyw test1
'Write a program that opens all'

py.exe mcb.pyw list
['test3','test2','test1']
'''

