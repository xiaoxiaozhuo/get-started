import urlparse
import urllib2
from bs4 import BeautifulSoup
#url='http://shop.nordstrom.com/c/women?origin=topnav&cm_sp=Top%20Navigation-_-Women-_-Women'
def findTab(url)
    response=urllib2.urlopen(url)
    html=response.read()
    soup=BeautifulSoup(html)
    l=soup.title.string
    hr=soup.find_all('a')
    for key in hr:
        temp=key.attrs['href']
        if temp[0]=='#':
            temp=urlparse.urljoin(url,temp)
        print temp
        print key.string

file=open("url.txt")
while 1:
    url=file.readline()
    findTab(url)
    if not line:
        break;
