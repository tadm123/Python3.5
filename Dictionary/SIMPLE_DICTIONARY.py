# "Automate the Boring Stuff" Book.
#CH 5 Exercises:

#Filling in a Dictionary.

name={}                            #initializing dictionary
while True:                          
    print('Type Key (type exit to exit):')
    i= input()
    if i == 'exit':
        break
    print('Type Value:')
    k= int(input())
    name[i]= k
    print(i +' : '  + str(k))

print('Fruit\t\tQuantity')
print('--------------------------')
for i,k in name.items():       #Printing the dictionary, where 'i' is key, 'k' is the value.
    print(i + '\t\t' + str(k))      
   

'''
#Putting a list of values into a Dictionary:

name={}
fruit = ['Bananas','Pears','Oranges','Apples']
num =  [10,4,23,5]

for i in range(len(fruit)):
    name[fruit[i]]= num[i]      #copying into dictionary

for i,k in name.items():        #print them
    print(i + '\t\t' + str(k)) 
'''
