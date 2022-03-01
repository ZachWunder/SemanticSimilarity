from ast import parse
from utils import computeSimilarities, log, parseTokensFromFile

f1 = parseTokensFromFile("crazynewideas.txt", "paragraph")
f2 = parseTokensFromFile("ideageneration.txt", "paragraph")

similarities = computeSimilarities(f1, f2)

log(similarities, f1, f2)

