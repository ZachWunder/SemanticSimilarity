from utils import computeSimilarities, log, parseTokensFromFile
import random
import os

pgarticles = []
for root, subdirs, files in os.walk('articles/pg'):
  pgarticles = files

saarticles = []
for root, subdirs, files in os.walk('articles/samaltman'):
  saarticles = files


for i in range(30):
  rand1 = random.randint(0,80)
  rand2 = random.randint(0,80)
  f1 = parseTokensFromFile("articles/pg/{}".format(pgarticles[rand1]), "paragraph")
  f2 = parseTokensFromFile("articles/samaltman/{}".format(saarticles[rand2]), "paragraph")

  similarities = computeSimilarities(f1, f2)

  log("Top3", similarities, f1, f2)

