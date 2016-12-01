# "Automate the Boring Stuff" Book
# CH10: stopwatch.pi - A Simple Stopwatch Program.

import time

#Display the program's instructions.
print(''''Press ENTER to begin. AFterwards, press ENTER to "click" the stopwatch.
Press Ctrl-C to quit.''')
input()         # press Enter to begin
print('Started.')
startTime = time.time()     # get the first lap's star time,  this will be a constant throughout the program
lastTime = startTime
lapNum= 1

# Start tracking the lap times.
try:    
    while True:
        input()                                       #click Enter to start the loop (2nd, 3rd, 4th laps ..)
        lapTime = round(time.time() - lastTime,2)      #time for each lap
        totalTime = round(time.time() - startTime,2)   #total time overall from beggining(startTime)
        print('Lap #%s: %s (%s)' %(str(lapNum).rjust(2), str(totalTime).rjust(5).ljust(6), str(lapTime).rjust(6)), end='')  #subs 
        lapNum += 1
        lastTime= time.time()      # reset the last lap time
except KeyboardInterrupt:
    #Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')



'''ex running program:
Lap #1: 1.48 (1.48)
Lap #2: 2.89 (1.41)
Lap #3: 5.0 (2.1)
Lap #4: 5.7 (0.69)
Lap #5: 6.24 (0.53)
Lap #6: 8.03 (1.78)
Lap #7: 8.62 (0.57)
Lap #8: 9.04 (0.41)
Lap #9: 9.32 (0.27)

Done. '''
