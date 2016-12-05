# "Automate the Boring Stuff" Book.
# CH9: os.walk() exercises.
# os.walk() of the directory c:\users\patty\desktio\loops
# Remember os.walk returns three values.
# 1. The root directory
#    2. A list of directories(dirs) immediately below the current root
#        3. A list of files found un those directories

import os

for folderName, subfolders, filenames in os.walk('c:\\users\\patty\\desktop\\loops'):
	print('The current folder is ' + folderName)
	for subfolder in subfolders:
		print('SUBFOLDER OF '+ folderName+ ': ' + subfolder)
	for filename in filenames:
		print('FILE INSIDE ' + folderName +': ' + filename)
	print('')


