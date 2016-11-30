# "Automate The Boring Stuff" Book
#  CH 4 Project: myPets.py
#  Check if your pet is on the list


import sys

myPets= []

while True:
    print('Enter a pet name (type \'quit\' to exit):')
    name = input()
    if name in myPets:
        print('Pet name already on list')
    elif name == 'quit':
        sys.exit()
    elif name == 'print':
        print('List of pets are: ')
        for i in range(len(myPets)):
            print(myPets[i], end=' ')
        print('')
    else:    
        myPets.append(name)
