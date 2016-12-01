# Simple program for creating and deleting files

import os, send2trash

os.chdir('c:\\users\\patty\\desktop')  #or os.chdir(os.path.join('users','patty','desktop'))

if not os.path.exists('Test'):
    os.makedirs('Test')

print('Type create(create files) or delete(delete files)')
print('Press CTRL-C to cancel')

try:
    while True:
        a = input('Command: ')
        number = input('Type number: ')
        if a == 'create':    
            for num in range(int(number)):
                filename = 'filename' + str(num) + '.txt'
                fp = open(os.path.join('Test',filename), 'w')
                print(filename)
                fp.write('This is a test')
                fp.close()
            
        elif a == 'delete':
            for num in range(int(number)):
                filename = 'filename' + str(num) + '.txt'
                print('Deleting... ' + filename)
                send2trash.send2trash(os.path.join('Test',filename))
            
except KeyboardInterrupt:     #Handles the Ctrol-C exception
    print('Exiting..')

