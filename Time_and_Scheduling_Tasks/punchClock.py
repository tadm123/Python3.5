# Program that simulates a timer for a job.
# Punch clock in and out

import time

print('Punch in to begin',end='')
input('')
print('Clock is starting')
startTime = time.time()

input()
print('Clock stopped')
lastTime = time.time()
print('Overall time is: %s' %(lastTime - startTime), end='')
