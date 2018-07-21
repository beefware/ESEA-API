from bs4 import BeautifulSoup
import cfscrape

URL = 'https://play.esea.net/users/'

def get_parsed_page(identifier):
    return cfscrape.create_scraper().get(URL + str(identifier)).content

def last_seen(identifier):
    source = get_parsed_page(identifier)
    soup = BeautifulSoup(source, "lxml")
    profile_header = soup.find("div", {"id": "profile-header"})
    contents = profile_header.find("h1").text.replace("\n", "").replace("\r", "").split('/')
    return contents[1]

def username_from_id(identifier):
    source = get_parsed_page(identifier)
    soup = BeautifulSoup(source, "lxml")
    profile_header = soup.find("div", {"id": "profile-header"})
    contents = profile_header.find("h1").text.replace("\n", "").replace("\r", "").split('/')
    return contents[0]

def get_karma(identifier):
    source = get_parsed_page(identifier)
    soup = BeautifulSoup(source, "lxml")
    karma = soup.find("span", {"id": "karma-1549397"}).getText()
    return karma
