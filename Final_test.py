from bs4 import BeautifulSoup
import requests as req


resp = req.get("https://ranobelib.me/bezdna")
soup = BeautifulSoup(resp.text, 'lxml')
# print(soup.prettify())
# print('----------------------------')
#print(soup.text.replace('\n', ' ').split('\n'))
for i in soup.text.split('\n'):
    if 'В закладках у людей' in i:
        print(i)
# a = soup.select('strong')
# print(a)
# print('----------------------------')
#
# print(soup.find_all(lambda a: 'manga-info' in a.get('class')))
#
# print('------------------------------')
tags = soup.find_all(['div', 'p'])
views = ''
for tag in tags:
    for j in tag.text.split():
        if 'просм' in j.lower():
            views = j
print(views)

