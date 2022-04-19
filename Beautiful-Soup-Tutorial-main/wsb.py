from bs4 import BeautifulSoup
import requests
import re

def doc(url):
    result = requests.get(url).text
    return BeautifulSoup(result, "html.parser")

print(doc("https://www.reddit.com/r/wallstreetbets/"))    
