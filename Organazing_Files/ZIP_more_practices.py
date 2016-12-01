# "Automate the Boring Stuff" Book
# CH9: Selective Copy Project
# Write a program that walks through a folder tree and searches for files with a 
# certain file extension (such as .pdf or .jpg). Copy these files from whatever location 
# they are in to a new folder.


#Add only .pdf files from the Desktop into the ZIP file 'PDFfiles.zip'

import zipfile,os

os.chdir('c:\\users\\patty\\desktop')
zp= zipfile.ZipFile('PDFfiles.zip', 'w')

for foldername, subfolders, filenames in os.walk('c:\\users\\patty\\desktop'):
	for filename in filenames:
		if '.pdf' in filename:
			print(filename)
			zp.write(os.path.join(foldername,filename))
	break
zp.close()		

# Note you don't do a for loop of all subfolders,if you did it would normally would print subfolder
# and below all the files. So instead it just prints all filenames of all main folder and subfolders
# in a long string.
# This is the reason why we put a break, so it just analyzes the files in the current folder (Desktop)


#---------------------------------------------------------------------------------------
'''
#Add all files except .txt and .exe from \\loops folder into the ZIP file 'Test.zip'

import zipfile,os

os.chdir('c:\\users\\patty\\desktop')
zp= zipfile.ZipFile('Test.zip', 'w')

for foldername, subfolders, filenames in os.walk('\\loops'):
	for filename in filenames:
		if not filename.endswith('.txt') and not filename.endswith('.exe'):
			print(filename)
			zp.write(os.path.join(foldername,filename))
    
zp.close()

'''
# ---------------------------------------------------------------------------------------



			
    
