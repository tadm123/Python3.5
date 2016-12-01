# "Automate The Boring Stuff" Book
# CH 5: Fantasy Game Inventory Project.
# You are creating a fantasy video game. The data structure to model
# the player’s inventory will be a dictionary where the keys are string values
# detailing how many of that item the player has. For example,the dictionary
# value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# means the player has 1 rope, 6 torches, 42 gold coins, and so on.

    
# Acessing the key(k) and value(k) in the for loop.

def displayInventory(invent):

    print('Inventory:')
    item_total = 0
    for k, v in invent.items():          
        item_total += invent.get(k,0)
        print(str(v)+ '\t'+ k)
    print("Total number of items: " + str(item_total))

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)

#Or using the get() function:

'''def displayInventory(invent):
    item_total=0
    print('Inventory:')
    for i in invent:
        item_total += invent.get(i,0)
        print(str(invent.get(i,0))+ '   ' + i)
    print('Total number of items: '+str(item_total))
    

         
inventory= {'rope':1, 'torch': 6, 'gold coin': 42, 'dagger':1, 'arrow':12}
displayInventory(inventory)
'''
