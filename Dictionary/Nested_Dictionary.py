# "Automate the Boring Stuff" book
# CH5 Exercise: Nested Dictionary. 
# Goes through the Dictionary and prints all items that are being brought to the picnic by the guests (Alice, Bob and Carol)

allGuests= {'Alice': {'apples':5, 'pretzels' : 12 },       #Guests brings different picnic items
            'Bob': {'ham sandwiches': 3, 'apples' :2},
            'Carol' : {'cups': 3, 'apple pies' :1 }}


def totalBrought(guests, item):
    numBrought= 0
                                                #Inside the loop, the string of the guest’s name is assigned to k, and the dictionary of picnic items they’re bringing is assigned to v
    for k,v in guests.items():                          #name.items() module get both key and value (name.keys() get only keys, name.values() get values
        numBrought = numBrought + v.get(item,0)         #go through the three members and adds the apples (if no 'apples' return 0) ..numBrought + 0
    return numBrought
    

print('Number of things being brought:')                                    
print(' - Apples          ' + str(totalBrought(allGuests, 'apples')))       #All apples being brought by all the guests
print(' - Cups            ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes           ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches  ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies      ' + str(totalBrought(allGuests, 'apple pies')))

