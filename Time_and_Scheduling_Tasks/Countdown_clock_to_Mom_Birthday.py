# "Automate the Boring Stuff" Book
# CH10: Countdown clock until Mom's birthday (November 14) Program

import datetime,time

MomBD = datetime.datetime(2016, 11, 14)
print('''Time left until Mom's Birthday: ''')
while datetime.datetime.now() < MomBD:
    print(str(MomBD- datetime.datetime.now()))
    time.sleep(1)
