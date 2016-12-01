# Daily Programer challenge:
# https://www.reddit.com/r/dailyprogrammer/comments/5bn0b7/20161107_challenge_291_easy_goldilocks_bear/

# Goldilocks challenge

import os

os.chdir('c:\\users\\patty\\desktop')
fp = open('goldilocks.txt')
list = fp.readlines()
fp.close()
weight= int(list[0].replace('\n','').split(' ')[0])
maxtemp= int(list[0].replace('\n','').split(' ')[1])

for i in range(1,len(list)):
    if ((weight <= int(list[i].replace('\n','').split(' ')[0]))
    and (maxtemp >= int(list[i].replace('\n','').split(' ')[1]))):
        print('%d ' %i, end='')









    
