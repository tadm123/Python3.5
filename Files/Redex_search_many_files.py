#Write a program that opens all .txt files in a folder and searches for any line
#that matches auser-supplied regular expression. The results should be printed to the screen.
#My regular expression will be to find sentences the contain the word 'What'

'''
import re,os

final_list = []

for filename in os.listdir('C:\\users\\patty\\desktop\\loops\\python_command'):
        if '.txt' in filename:
                fp= open('c:\\users\\patty\\desktop\\loops\\python_command\\' + filename)
                content= fp.readlines()   #reads lines of a file and puts them in the 'contents' list
                for i in range(len(content)):
                        #Regex = re.compile(r'(variable)')
                        #mo= Regex.findall(
                        if 'What' in content[i]:
                                final_list.append(content[i])           #adds lines that have 'What' into the 
                fp.close()                                              #'final_list' list by using .append adding elements

list= '\n'.join(final_list)                     #joins all list
print(list)



'''
# Here matching any word that starts with 'p'

import re,os

mo= []
os.chdir('C:\\users\\patty\\desktop\\loops\\python_command')  #changes the directory to here

for filename in os.listdir():
        if '.txt' in filename:
                fp= open(filename)
                content= fp.read()   #reads the whole string and puts them one huge string in 'contents'               
                regex= re.compile(r'\s(p\w+)')          #words that begin with 'p'
                mo+= regex.findall(content)
                fp.close()  
                                                    

list= '\n'.join(mo)                     #joins all list
print(list)









