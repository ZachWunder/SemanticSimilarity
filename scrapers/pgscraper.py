import requests
from bs4 import BeautifulSoup

URL = "http://www.paulgraham.com/articles.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

for a in soup.find_all('a', href=True):
  link = a['href']
  articleURL = "http://www.paulgraham.com/{}".format(link)
  articlePage = requests.get(articleURL)
  articleSoup = BeautifulSoup(articlePage.content, "html.parser")
  text = articleSoup.find("font").get_text()
  file = open("articles/{}.txt".format(link.split('.')[0]), 'w')
  file.write(text)

# trs = soup.find('table').find_all('tr')
# for tr in range(len(trs)):
#   if tr % 2 != 0 and tr != 1:
#     print(trs[tr].find_all('a'))