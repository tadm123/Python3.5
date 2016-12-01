# "Automate The Boring Stuff" Book
# CH 5: Fantasy Game Inventory
# List to Dictionary Function for Fantasy Game Inventory



def addToInventory(inventory, addedItems):


 for i in addedItems:
       
       if i in inventory.keys():            #if the name already exist
            inventory[i]=inventory[i]+1     #add 1 to its quantity
       else:
            inventory[i] = 1                #Create another item in the dictionary

 return inventory

    
  
def displayInventory(inventory):

    num=0
    print('Inventory:')
    for k,v in inventory.items():
        print(str(v) + '\t' + k)
        num += v

    print('')
    print('Total number of items: ' + str(num))



inv = {'gold coin': 42, 'rope': 1}                                         #dictionary containing the item and the quantity
dragonLoot= ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']      #a list of items

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)

