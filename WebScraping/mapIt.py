# "Automate the Boring Stuff" Book
# CH8: mapIt.py   - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from comand line.
    address = ' '.join(sys.argv[1:])  #You don’t want the program name in this string, so instead of
                                      #sys.argv, you should pass sys.argv[1:]
else:
    #Get address from clipboard.
    address= pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
