# "Automate the Boring Stuff" book
# CH10: logging module Exercise.
# Using different logging levels to debug a program.


import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total =1
    for i in range(1,n+1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' +str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')



'''
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

dict= {'Daniel':26, 'Melinda': 24, 'Mark': 54, 'Jacob': 34}

for names in dict.keys():
    logging.debug(names + ' age: ' + str(dict[names])) 
    
'''
