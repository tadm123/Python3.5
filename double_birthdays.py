# double_birthdays.py - Calculate double birthdays

# This program calculates the probability of two students having the same birthday.
# Input the number of students that you wish to sample.
# This problem is based on the 'Birthday paradox' https://en.wikipedia.org/wiki/Birthday_problem

import random

NUM_OF_SAMPLES = 10000
NUM_DAYS_IN_A_YEAR = 365

def checking(my_dict):                  #returns 1 if the sample has double birthdays (or more), if not returns 0
      for i in my_dict.values():
              if i >= 2:
                      return 1
      return 0

check = []      
count = 0
NUM_OF_STUDENTS = int(input('Number of students(sample size): '))
for i in range(NUM_OF_SAMPLES):
      my_dict = {}
      for i in range(NUM_OF_STUDENTS):                                                   
              num = random.randint(1,NUM_DAYS_IN_A_YEAR)
              if num not in my_dict.keys():
                      my_dict[num]= 1
              else:
                      my_dict[num] = my_dict[num] + 1
      check.append(checking(my_dict))
      
for i in check:                 #
	if i == 1:
		count+=1              
#--------------------------------------------
#Computation for theory

def factorial(num):   
	if num == 0:
		return 1
	else:
		return num * factorial(num-1)

p_ = factorial(365)/((365**NUM_OF_STUDENTS)*factorial(365-NUM_OF_STUDENTS))      
p = round((1 - p_) *100,5)
#-------------------------------------------------

Percentage = round(count / len(check) * 100,5)
print('\n')
print('Chance of double birthdays sampling it %s times: %%%s' %(NUM_OF_SAMPLES,Percentage))
print('Theoretical chance: %%%s\n' %p)

'''
#Peering into the results from a single sample:                 

sum=0
print('Result from a single sample:')
print(' Student     Frequecy')       #Data just 1 sample
print('Birthday           ')
for num,freq in my_dict.items():
	print('%s\t\t%s' %(str(num).rjust(6),str(freq).rjust(1)))
	sum=sum+freq
'''


