from pprint import pprint

import requests
from bs4 import BeautifulSoup

url='https://www.example.com/data.csv'
# url='https://docs.docker.com/language/python/build-images/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('body').text

#pprint(title)
print(title)
