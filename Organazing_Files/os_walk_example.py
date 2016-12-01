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



''' Output:

The current folder is c:\users\patty\desktop\loops
SUBFOLDER OF c:\users\patty\desktop\loops: New_dir
SUBFOLDER OF c:\users\patty\desktop\loops: python_command
FILE INSIDE c:\users\patty\desktop\loops: a.exe
FILE INSIDE c:\users\patty\desktop\loops: address.exe
FILE INSIDE c:\users\patty\desktop\loops: address_program.c
FILE INSIDE c:\users\patty\desktop\loops: analyze.c
FILE INSIDE c:\users\patty\desktop\loops: analyze.exe
FILE INSIDE c:\users\patty\desktop\loops: canopen.c
FILE INSIDE c:\users\patty\desktop\loops: canopen.exe
FILE INSIDE c:\users\patty\desktop\loops: canopen.o
FILE INSIDE c:\users\patty\desktop\loops: clearsample.exe
FILE INSIDE c:\users\patty\desktop\loops: clear_sample.c
FILE INSIDE c:\users\patty\desktop\loops: clear_sample.exe
FILE INSIDE c:\users\patty\desktop\loops: clear_sample.o
FILE INSIDE c:\users\patty\desktop\loops: comparing_dates.c
FILE INSIDE c:\users\patty\desktop\loops: convert.exe
FILE INSIDE c:\users\patty\desktop\loops: convert_date.c
FILE INSIDE c:\users\patty\desktop\loops: convert_to_upper.c
FILE INSIDE c:\users\patty\desktop\loops: copy.txt
FILE INSIDE c:\users\patty\desktop\loops: date.exe
FILE INSIDE c:\users\patty\desktop\loops: demo.c
FILE INSIDE c:\users\patty\desktop\loops: demo.exe
FILE INSIDE c:\users\patty\desktop\loops: Downloads - Shortcut.lnk
FILE INSIDE c:\users\patty\desktop\loops: encrypt.exe
FILE INSIDE c:\users\patty\desktop\loops: fcat.c
FILE INSIDE c:\users\patty\desktop\loops: fcat.exe
FILE INSIDE c:\users\patty\desktop\loops: fcopy.c
FILE INSIDE c:\users\patty\desktop\loops: fcopy.exe
FILE INSIDE c:\users\patty\desktop\loops: fcopy.o
FILE INSIDE c:\users\patty\desktop\loops: first.dat
FILE INSIDE c:\users\patty\desktop\loops: GCD_structures.c
FILE INSIDE c:\users\patty\desktop\loops: invclear.c
FILE INSIDE c:\users\patty\desktop\loops: invclear.exe
FILE INSIDE c:\users\patty\desktop\loops: invclear.o
FILE INSIDE c:\users\patty\desktop\loops: Inventory2.c
FILE INSIDE c:\users\patty\desktop\loops: inventory2.exe
FILE INSIDE c:\users\patty\desktop\loops: justify.c
FILE INSIDE c:\users\patty\desktop\loops: justify.exe
FILE INSIDE c:\users\patty\desktop\loops: justify.o
FILE INSIDE c:\users\patty\desktop\loops: line.c
FILE INSIDE c:\users\patty\desktop\loops: line.h
FILE INSIDE c:\users\patty\desktop\loops: line.o
FILE INSIDE c:\users\patty\desktop\loops: merge.c
FILE INSIDE c:\users\patty\desktop\loops: merge.exe
FILE INSIDE c:\users\patty\desktop\loops: moretest.txt
FILE INSIDE c:\users\patty\desktop\loops: mytest.exe
FILE INSIDE c:\users\patty\desktop\loops: my_test.c
FILE INSIDE c:\users\patty\desktop\loops: my_test.exe
FILE INSIDE c:\users\patty\desktop\loops: my_test.o
FILE INSIDE c:\users\patty\desktop\loops: newmsg.txt
FILE INSIDE c:\users\patty\desktop\loops: newquote.txt
FILE INSIDE c:\users\patty\desktop\loops: output.dat
FILE INSIDE c:\users\patty\desktop\loops: planets.c
FILE INSIDE c:\users\patty\desktop\loops: planets.exe
FILE INSIDE c:\users\patty\desktop\loops: pun.c
FILE INSIDE c:\users\patty\desktop\loops: read_line.c
FILE INSIDE c:\users\patty\desktop\loops: read_line.h
FILE INSIDE c:\users\patty\desktop\loops: remind.c
FILE INSIDE c:\users\patty\desktop\loops: remind2.c
FILE INSIDE c:\users\patty\desktop\loops: remind2.exe
FILE INSIDE c:\users\patty\desktop\loops: remind2.o
FILE INSIDE c:\users\patty\desktop\loops: reverse.c
FILE INSIDE c:\users\patty\desktop\loops: reverse.exe
FILE INSIDE c:\users\patty\desktop\loops: reverse.o
FILE INSIDE c:\users\patty\desktop\loops: second.dat
FILE INSIDE c:\users\patty\desktop\loops: something.c
FILE INSIDE c:\users\patty\desktop\loops: something.exe
FILE INSIDE c:\users\patty\desktop\loops: something.txt
FILE INSIDE c:\users\patty\desktop\loops: sonnet.txt
FILE INSIDE c:\users\patty\desktop\loops: test.c
FILE INSIDE c:\users\patty\desktop\loops: test.txt
FILE INSIDE c:\users\patty\desktop\loops: testing.txt
FILE INSIDE c:\users\patty\desktop\loops: untitled.txt
FILE INSIDE c:\users\patty\desktop\loops: untitled2.txt
FILE INSIDE c:\users\patty\desktop\loops: untitled_2.txt
FILE INSIDE c:\users\patty\desktop\loops: word.c
FILE INSIDE c:\users\patty\desktop\loops: word.h
FILE INSIDE c:\users\patty\desktop\loops: XOR.exe
FILE INSIDE c:\users\patty\desktop\loops: XOR.o

The current folder is c:\users\patty\desktop\loops\New_dir
FILE INSIDE c:\users\patty\desktop\loops\New_dir: -
FILE INSIDE c:\users\patty\desktop\loops\New_dir: capitalsquiz1.txt
FILE INSIDE c:\users\patty\desktop\loops\New_dir: capitalsquiz2.txt
FILE INSIDE c:\users\patty\desktop\loops\New_dir: capitalsquiz3.txt
FILE INSIDE c:\users\patty\desktop\loops\New_dir: capitalsquiz_answers1.txt
FILE INSIDE c:\users\patty\desktop\loops\New_dir: capitalsquiz_answers2.txt
FILE INSIDE c:\users\patty\desktop\loops\New_dir: capitalsquiz_answers3.txt
FILE INSIDE c:\users\patty\desktop\loops\New_dir: mcb.bak
FILE INSIDE c:\users\patty\desktop\loops\New_dir: mcb.dat
FILE INSIDE c:\users\patty\desktop\loops\New_dir: mcb.dir
FILE INSIDE c:\users\patty\desktop\loops\New_dir: mcb.pyw
FILE INSIDE c:\users\patty\desktop\loops\New_dir: msg_renamed.txt
FILE INSIDE c:\users\patty\desktop\loops\New_dir: myData.bak
FILE INSIDE c:\users\patty\desktop\loops\New_dir: myData.dat
FILE INSIDE c:\users\patty\desktop\loops\New_dir: myData.dir
FILE INSIDE c:\users\patty\desktop\loops\New_dir: My_test.txt
FILE INSIDE c:\users\patty\desktop\loops\New_dir: pw.py
FILE INSIDE c:\users\patty\desktop\loops\New_dir: second.dat
FILE INSIDE c:\users\patty\desktop\loops\New_dir: second.dir
FILE INSIDE c:\users\patty\desktop\loops\New_dir: sonnet.txt
FILE INSIDE c:\users\patty\desktop\loops\New_dir: testing.bat
FILE INSIDE c:\users\patty\desktop\loops\New_dir: testing.py
FILE INSIDE c:\users\patty\desktop\loops\New_dir: trying.txt
FILE INSIDE c:\users\patty\desktop\loops\New_dir: xor.c

The current folder is c:\users\patty\desktop\loops\python_command
FILE INSIDE c:\users\patty\desktop\loops\python_command: -
FILE INSIDE c:\users\patty\desktop\loops\python_command: capitalsquiz1.txt
FILE INSIDE c:\users\patty\desktop\loops\python_command: capitalsquiz2.txt
FILE INSIDE c:\users\patty\desktop\loops\python_command: capitalsquiz3.txt
FILE INSIDE c:\users\patty\desktop\loops\python_command: capitalsquiz_answers1.txt
FILE INSIDE c:\users\patty\desktop\loops\python_command: capitalsquiz_answers2.txt
FILE INSIDE c:\users\patty\desktop\loops\python_command: capitalsquiz_answers3.txt
FILE INSIDE c:\users\patty\desktop\loops\python_command: mcb.bak
FILE INSIDE c:\users\patty\desktop\loops\python_command: mcb.dat
FILE INSIDE c:\users\patty\desktop\loops\python_command: mcb.dir
FILE INSIDE c:\users\patty\desktop\loops\python_command: mcb.pyw
FILE INSIDE c:\users\patty\desktop\loops\python_command: msg_renamed.txt
FILE INSIDE c:\users\patty\desktop\loops\python_command: myData.bak
FILE INSIDE c:\users\patty\desktop\loops\python_command: myData.dat
FILE INSIDE c:\users\patty\desktop\loops\python_command: myData.dir
FILE INSIDE c:\users\patty\desktop\loops\python_command: My_test.txt
FILE INSIDE c:\users\patty\desktop\loops\python_command: pw.py
FILE INSIDE c:\users\patty\desktop\loops\python_command: second.dat
FILE INSIDE c:\users\patty\desktop\loops\python_command: second.dir
FILE INSIDE c:\users\patty\desktop\loops\python_command: sonnet.txt
FILE INSIDE c:\users\patty\desktop\loops\python_command: testing.bat
FILE INSIDE c:\users\patty\desktop\loops\python_command: testing.py
FILE INSIDE c:\users\patty\desktop\loops\python_command: trying.txt
FILE INSIDE c:\users\patty\desktop\loops\python_command: xor.c

'''
