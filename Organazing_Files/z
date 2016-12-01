# "Automate the Boring Stuff" Book
# CH9: Project: Disk Space. 
# Find the folder in a directory tree that has the greatest number of files or the folder that uses the most disk space

import os

os.chdir('c:\\users\\patty\\desktop')   #change to directory where you want to sweep all files
size= 0

for foldername, subfolders, filenames in os.walk('c:\\users\\patty\\desktop\\loops'):
        print('Current folder: %s' %(foldername))
   # for subfolders in subfolder
        for filename in filenames:
            size += os.path.getsize(os.path.join(foldername,filename))
        print('Size: %d' %(size))
        print('Setting size = 0 ')
        size=0
    
