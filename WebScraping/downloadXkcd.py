# "Automate the Boring Stuff" Book
# CH8: downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url= 'http://xkcd.com'                          # starting url
os.chdir('c:\\users\\patty\\desktop')
os.makedirs('xkcd', exist_ok = True)            # store comics in ./xkcd
while not url.endswith('#'):
    #Download the page.
    print('Downloading page %s...' %url)
    res = requests.get(url)                     #put the main url here  (.gets is used for this)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")       #or just (res.text)

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')       #put the image here (.select is used to parse the url)
                                                #<div id = "comic"> == $0
                                                #    <img src = "//imgs.xkcd.com/comics/mushrooms.png" title...
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            #Download the image.
            print('Downloading image %s...' %(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            #skip this comic
            prevLink = soup.select('a[rel = "prev"]')[0]    #All elements named <a> that have an attribute named rel with value prev (note [0] gets you only the first element found of the list, [1] would be the second etc)
            url = 'http://xkcd.com' + prevLink.get('href')  # ex: <a rel = "prev" href="/1747/"  <- 1747 is the previous page (http:/xcld.com/1747)
            continue

        #Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    #Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
