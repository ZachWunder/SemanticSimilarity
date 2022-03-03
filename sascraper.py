import requests
from bs4 import BeautifulSoup

for page in range(1, 10):
  URL = "https://blog.samaltman.com/?page={}".format(page)
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")

  posts = []
  postTitle = []
  for postBody in soup.find_all("div", {"class": "post-body"}):
    posts.append(postBody.get_text())
  
  for postTitle in soup.find_all("div", {"class": "post-title"}):
    postTitle.append(postTitle.get_text())

  f = open("articles/samaltman/{}".format())
