#!/bin/python3
print("get.py by Elias Eskelinen aka jonnelafin")
from bs4 import BeautifulSoup
import requests

def match_class(target):
	def do_match(tag):
		classes = tag.get('class', [])
		return all(c in classes for c in target)
	return do_match
print("Getting the page...")
url = 'https://yle.fi/uutiset/18-212923'
page = requests.get(url)
soup = BeautifulSoup(page.content, features="html.parser")
print("Fetching...")
links = soup.find_all(match_class(["yle__article__listItem__link"]))
#print(soup)
olinks = []
print("Saving...")
for s in links:
	o = str(s).split("href=\"")[1].split("\">")[0]
	olinks.append("https://yle.fi"+o)
with open("links.txt", "w+") as f:
	for i in olinks:
		f.write(i + "\n")
	#	print(i)
	f.close()
print("Saved " + str(len(olinks)) + " entries.")
print("Have a good day.")
