# This program downloads all the links from a subreddit


import requests, os, bs4

print('******  This program downloads all link from a subreddit  ********')


while True:                             #We test if the subreddit exists, if it doesn't you input another one
    print('Enter a subreddit:')
    subreddit = input()
    res = requests.get('https://www.reddit.com/subreddits/search?q=' + subreddit, headers = {'User-agent': 'your bot 0.1'})
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    Elem = soup.select('#noresults')

    if Elem:
        print('Subreddit doesn\'t exist.')
        print('Try again')
        continue
    break


url= 'https://www.reddit.com/r/' + subreddit   #example url
os.chdir('c:\\users\\patty\\desktop')          #choose location where you want to store your folder containing the .txt file
if not os.path.isdir('RedditLinks'):
    os.makedirs('RedditLinks')

res= requests.get(url, headers = {'User-agent': 'your bot 0.1'})   #This fixes 404 problem
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

linkElem= soup.select('.title.may-blank')
fp= open('RedditLinks\\'+subreddit+'links.txt','w')
fp.write('~~~~~~~~~~~~   Links from ' + url+ ' ~~~~~~~~~~~~~\n\n\n')
for i in range(len(linkElem)):
    a= linkElem[i].get('href')
    if not a.startswith('http'):
        a= 'https://www.reddit.com' + a    
    print(a)
    fp.write(a)
    fp.write('\n')
print('Done')
fp.close()
        

    
