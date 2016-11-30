# "Automate the Boring Stuff" book - password.py
# Enter a password.

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():     #check if its a number
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password=input()
    if password.isalnum():      #isalnum() check if a string consists of letters and numbers and is not blank
        break
    print('Passwords can only have letters and numbers.')
