import sys
import requests
import time
from lxml import html

website = requests.get('https://twitter.com/onedirection?lang=fr')
tree=html.fromstring(website.content)
followers=tree.xpath("//a[@data-nav='followers']/span/@data-count")[0]
    
date = time.strftime("%d/%m/%Y")
heure = time.strftime("%H:%M:%S")
print(str(followers) + ' ' + date + ' ' + heure)