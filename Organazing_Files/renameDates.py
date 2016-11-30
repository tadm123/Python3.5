# "Automate the Boring Stuff" Book
# CH9: renameDates.oy  - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

#Create a regex that matches files with the American date format.

datePattern= re.compile(r'''^(.*?)    # all text before the date
    ((0|1)?\d)-                       # one or two digits for the month
    ((0|1|2|3)?\d)-                   # one or two digits for the day
    ((19|20)\d\d)                     # four digits for the year
    (.*?)$                            # all text after the date
    ''', re.VERBOSE)

# remember ?  -> matches zero or of the preceding group
#          .* -> matches any characters (except a newline)
#           *   -> matches zero or more of the prceding group   pg.162


#Loop over the files in the working directory.
os.chdir('c:\\users\\patty\\desktop\\loops\\python_command')
for amerFilename in os.listdir('.'):
    mo= datePattern.search(amerFilename)

    if mo == None:              #Skip files without date
        continue

    #Get the different parts of the filename.
    beforePart= mo.group(1)     
    monthPart = mo.group(2) 
    dayPart   = mo.group(4)
    yearPart  = mo.group(6)
    afterPart = mo.group(8)

    #Form the European-style filename.
    euroFilename= beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    #Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')        #gets absolute path of '.', which means 'this directory'
    amerFilename = os.path.join(absWorkingDir, amerFilename)     #os.path.join is helpful when you need to create strings for filenames
    euroFilename = os.path.join(absWorkingDir, euroFilename)     #c\\users\\patty\\loops\\24-12-2005_list.txt

    #Rename the files
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
