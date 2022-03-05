import requests
from bs4 import BeautifulSoup

posts = []
postTitles = []

for page in range(1, 10):
  URL = "https://blog.samaltman.com/?page={}".format(page)
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")

  for postBody in soup.find_all("div", {"class": "post-body"}):
    posts.append(postBody.get_text())
  
  for postTitle in soup.find_all("div", {"class": "post-title"}):
    title = postTitle.get_text()
    postTitles.append(title.strip())


for post in range(len(posts)):
  f = open("articles/samaltman/{}.txt".format(postTitles[post]), 'w')
  f.write(posts[post])
  f.close()