import requests
import time
from lxml import html

class Scores:
	def __init__(self):
		self.followers=followers
		
	def followers(self):
		website = requests.get('https://twitter.com/onedirection?lang=fr')
		tree=html.fromstring(website.content)
		self.followers=tree.xpath("//a[@data-nav='followers']/span/@data-count")[0]
		return self.followers