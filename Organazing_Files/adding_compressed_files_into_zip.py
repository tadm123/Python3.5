# "Automate the Boring Stuff" Book
# CH9: Adding compressed files and folders into zip 'new.zip' in Desktop


import zipfile,os

os.chdir('c:\\users\\patty\\desktop')          #Going to desktop
zp= zipfile.ZipFile('new.zip', 'a')            
                                                   
for foldername, subfolders, filenames in os.walk('c:\\users\\patty\\desktop\\My_files'):
    print('Adding current folder : %s' % (foldername))
    zp.write(foldername)
    for subfolder in subfolders:
        print('Subfolder: ' +os.path.join(foldername,subfolder))
        zp.write(os.path.join(foldername,subfolder),compress_type= zipfile.ZIP_DEFLATED)
    for filename in filenames:
        print('Files: ' + os.path.join(foldername,filename))
        zp.write(os.path.join(foldername,filename),compress_type = zipfile.ZIP_DEFLATED)
        
zp.close()


# Now we will read this 'new.zip' ZIP file as practice and print its file size comparing it to its compress size
print('----------------------- Reading --------------------------\n')
zp = zipfile.ZipFile('new.zip', 'r')
print('Inside the zip: ')

for i in zp.namelist():
    print(i)

size = sum([zinfo.file_size for zinfo in  zp.filelist])
size_c = sum([zinfo.compress_size for zinfo in  zp.filelist])

print('\n\nSize(bytes) of all files in new.zip: ')
print('Its regular size: ' + str(size))
print('Its compressed size: ' + str(size_c))
zp.close()


# Note: It repeats the file because it first copies the 'c:\users\patty\desktop\My_files\Testing' as a subfolder
# of the current folder you are in (My_files) into the ZIP.
# In the next iteration when you change the current folders so your root folder is now My_files, it then copies it again



