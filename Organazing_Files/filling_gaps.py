# "Automate the Boring Stuff" Book
# CH9 Project: Filling in the Gaps.
# This programs finds gaps of numbers between the filenames and renames them appropiately.
# Ex: if you have spam001.txt and spam004.txt, it will rename spam004.txt into spam002.txt

def check(a):
        if a == None:
               return ''
        else:
                return a


import os,re,shutil


os.chdir('c:\\users\\patty\\desktop\\loops\\New_dir')


Regex= re.compile(r'(.*?)([0]+)?(\d+)(.*)?')
dict= {}

os.makedirs('c:\\users\\patty\\desktop\\loops\\Corrected_folder')
        
for filename in os.listdir('c:\\users\\patty\\desktop\\loops\\New_dir'):         #'spam002.txt'  and 'spam008.txt'
       
        mo = Regex.search(filename)
        if mo == None:
                continue
        
        firstpart= mo.group(1)         # 'spam'     'spam'
        zeros    = mo.group(2)         # '00'       '00'
        num      = int(mo.group(3))    # 2          8
        lastpart = mo.group(4)         # '.txt'     '.txt'

       
        zeros= check(zeros)
        
        
        if firstpart not in dict.keys():
                dict[firstpart]= [zeros,num,lastpart]     #dict = {'spam': ['00','2','.txt']} Just need this for the 1st iteration so it has something to compare
                shutil.copy(filename, 'c:\\users\\patty\\desktop\\loops\\Corrected_folder')
        else:
                if num != (dict[firstpart][1]+1):            #if 8 != (2+1=3) 
                        num= dict[firstpart][1] + 1           #num= 3 instead of 8
                        dict[firstpart]= [zeros,num,lastpart]
                        file= firstpart+zeros+str(num)+lastpart  # file = 'spam003.txt'
                        shutil.copy(filename, 'c:\\users\\patty\\desktop\\loops\\Corrected_folder\\'+file)

                                                                
    
