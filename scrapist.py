import requests
from bs4 import BeautifulSoup

r = requests.get('https://tabs.ultimate-guitar.com/tab/bruno-mars/when-i-was-your-man-chords-1198871')

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify)