from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

url = 'https://www.inshorts.com/en/read'
uClient = uReq(url)

page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

title = page_soup.findAll("div",{"class":"news-card-title news-right-box"})
read_more = page_soup.findAll("div",{"class":"read-more"})


i = 0
for i in range(len(title)):
    print(i+1, ". " + title[i].span.text)
    d = str(read_more[i]).split('href="')[1].split('?utm_campaign')[0]
    print("Read more at - " + d)
    i+= 1
    if i == 10:
      break
    else:
      print("-------------------------------------------------------------------")