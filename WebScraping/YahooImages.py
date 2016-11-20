# This program downloads images from Yahoo. Type number of photos you want to download and next
# the keyword.   ex:   YahooImages.py 4 Puppy

import os, requests, bs4, sys

os.chdir('c:\\users\\patty\\desktop')
if not os.path.isdir('YahooImages'):
    os.makedirs('YahooImages')


my_search = sys.argv[2:]
if len(sys.argv) == 1:
    print('Please enter a keyword')
    sys.exit()


res = requests.get('https://images.search.yahoo.com/search/images?p=' + ' '.join(my_search))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text , "html.parser")


'''
num=1
while os.path.exists('c:\\users\\patty\\desktop\\pictures\\%s%s.jpg' %(my_search,num)):
    num += 1
'''
print('Downloading images...')
for i in range(int(sys.argv[1])):
  
    Elem = soup.select('#resitem-fpub'+str(i)+' a img[src]')
    imgUrl = Elem[0].get('src')
    res = requests.get(imgUrl)
    res.raise_for_status()
    print(imgUrl)
    imgFile = open('c:\\users\\patty\\desktop\\YahooImages\\' + '_'.join(my_search) + str(i)+ '.jpg', 'wb')
    for chunk in res.iter_content(100000):
        imgFile.write(chunk)

    imgFile.close()
