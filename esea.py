import requests
from bs4 import BeautifulSoup
import cfscrape

def get_parsed_page(self, url):
	scraper = cfscrape.create_scraper()
	return scraper.get(url).content

def LastOnline(self, id):
	url = 'https://play.esea.net/users/{}'.format(id)
	soup = BeautifulSoup(self.get_parsed_page(url), "lxml")
	lo = soup.find("div", {"id": "profile-header"}).find("h1").text.replace("\n", "").replace("\r", "").split('/')
	return lo[1]

def UserName(self, id):
	url = 'https://play.esea.net/users/{}'.format(id)
	soup = BeautifulSoup(self.get_parsed_page(url), "lxml")
	lo = soup.find("div", {"id": "profile-header"}).find("h1").text.replace("\n", "").replace("\r", "").split('/')
	return lo[0]
