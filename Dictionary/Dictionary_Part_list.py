birthdays = {'Alice' : 'Apr 1', 'Bob' :'Dec 12', 'Carol':'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name= input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name]=bday
        print('Birthday database updated.')
"""
inventory= {}
    print('Enter a part number:')
    num= int(input())
    if str(name)== '':
        break
    print('What is the name of the part?')
    part=input()
    inventory[num]= part 



birthdays
{'Bob': 'Dec 12', 'Carol': 'Mar 4', 'Alice': 'Apr 1'}
>>> birthdays['Mariah']='April 23'
>>> birthdays
{'Bob': 'Dec 12', 'Carol': 'Mar 4', 'Alice': 'Apr 1', 'Mariah': 'April 23'} '''

"""
