from utils import parseTokensFromFile
from sentence_transformers import SentenceTransformer
import json
import frontmatter

model = SentenceTransformer('all-mpnet-base-v2')

article = frontmatter.load("sa_successful.txt")
tokens = article.content.split(".")

encoding = model.encode(tokens)

vectors = []
for i, embedding in enumerate(encoding):
  vectors.append(
    {
      "id": "pg-words-{}".format(i),
      "metadata": {
        "author": article["author"],
        "title": article["title"],
        "sentence": tokens[i]
      },
      "values": embedding.tolist()
    }
  )
  
finished = {
  "vectors": vectors
}
  
with open('embeddings.json', 'w') as outfile:
    json.dump(finished, outfile)

  
