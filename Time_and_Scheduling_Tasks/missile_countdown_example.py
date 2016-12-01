# missile_countdown.py - A simple countdown script
# missile_alarm.wav file was downloaded from http://soundbible.com/tags-missile.html

import time, subprocess, os
#os.chdir('c:\\users\\patty\\desktop')
timeLeft= 5
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1

print('\n********** Starting Missile Countdown *************')
# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'c:\\users\\patty\\desktop\\missile_alarm.wav'], shell=True)
