#A generic Webscraper shell
#Don't change this. Standard importing things
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
from datetime import datetime
#Just change the URL here
my_url = 'https://www.baseball-reference.com/leagues/MLB/2018-win_probability-pitching.shtml'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#HTML Parsing, no need to change this
page_soup = soup(page_html, "html.parser")
#Grabs what you want. Change HTML type and label
headers = ("Tm","RA/G","PtchR","PtchW","Plays","WPA","WPA+","WPA-","aLI","WPA/LI","Clutch","RE24","REW","boLI","RE24/boLI","LevHi","LevMd","LevLo")
teams = page_soup.findAll("th","class":"left")
datapoints = page_soup.findAll("td","class":"right")
	for
print(datapoints)
