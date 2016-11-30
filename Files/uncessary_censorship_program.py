# Unnecessary censorship Program.
# This program writes multiple files from clipboard into a File.
# and checks for any word that starts with 'f' or 's' and replaces it with f**** or s***

import pyperclip,re,os

os.chdir('C:\\users\\patty\\desktop\\loops\\python_command')  #changes the directory 

File= open('My_test.txt','a')

i=0
j=0
array = ['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth'
    'Nine','Tenth']

while True:
    print('Copy a file to clipboard and type \'w\'. Press \'q\' to quit')
    a= str(input())
    print(a) 
    if a == 'q':
        break
    elif a == 'w':
        text=str(pyperclip.paste())

        File.write('-------- %s unnecessary censorship ---------\n\n' %array[i])
        Regex= re.compile(r'\s(f)\w+|\s(s)\w+')
        new_text= Regex.sub(r' \1\2****', text)

        list= new_text.split()

        new_text= ''
        for j in range(len(list)):
            
            new_text += list[j] +' '
            if(j % 13 == 0 and j != 0):         #every 13 words
                 new_text += '\n'
             
        File.write(new_text)
        File.write('\n\n')
        i+=1
        print('Clipboard text was written into file')
            
    else:
        print('Please enter an appropiate command')


File.close()



#Note it seems that the copied text into the file is one long sting without any newlines
#to fix this problem, maybe you can store each word into a list (split function) and the
#print a new line every 13 words. So your text is formatted nicely.
''' Ex, maybe :
text=  
list= text.split()

new_text= ''
for i in range(len(list)):
        new_text += list[i] +' '
        if(i % 13 == 0 and i != 0):
             new_text += '\n'
        
    
print(new_text)

'''
