from ast import parse
from utils import computeSimilarities, log, parseTokensFromFile

f1 = parseTokensFromFile("articles/crazynewideas.txt", "paragraph")
f2 = parseTokensFromFile("articles/ideageneration.txt", "paragraph")

similarities = computeSimilarities(f1, f2)

log("CrazyNewIdeas_IdeaGeneration_Paragraph", similarities, f1, f2)

