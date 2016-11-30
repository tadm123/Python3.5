# Downloads images from http://www.verseoftheday.com/ and saves it into a DailyBibleVerse folder 

import requests, os, bs4

os.chdir('c:\\users\\patty\\desktop')       #modify location where you want to create the folder
if not os.path.isdir('DailyBibleVerse'):
    os.makedirs('DailyBibleVerse')

res = requests.get('http://www.verseoftheday.com/')     #Downloading the page into the 'res' variable
res.raise_for_status()

soup= bs4.BeautifulSoup(res.text, "html.parser")

#BibleCaption= soup.select('#featured .bilingual-left')   #If you want verse use this
#text= BibleCaption[0].getText()

BibleElem = soup.select('#tv-image-wrapper img')         #searching the image
BibleUrl= BibleElem[0].get('src')

num=1
while os.path.exists('c:\\users\\patty\\desktop\\DailyBibleVerse\\verse%s.jpg' %num):
    num += 1
    
File = open('c:\\users\\patty\\desktop\\DailyBibleVerse\\' +'verse'+ str(num)+ '.jpg', 'wb')  #this is the name
#if os.path.isfile('c:\\users\\patty\\desktop\\DailyBibleVerse\\'): how to add a number if file already exists?

res = requests.get(BibleUrl)

for chunk in res.iter_content(100000):
    File.write(chunk)
File.close()



