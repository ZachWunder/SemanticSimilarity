from sentence_transformers import SentenceTransformer, util
from datetime import datetime
model = SentenceTransformer('all-mpnet-base-v2')

# tokenType = sentence | paragraph | file
def parseTokensFromFile(path, tokenType):
    if tokenType == "sentence":
        text_file= open(path,'r')
        data=text_file.read()
        listOfSentences = data.split(".")
        return listOfSentences
    elif tokenType == "paragraph":
        valueToBeRemoved = ''
        file = open(path, "r")
        sentences = file.read().splitlines()
        sentences = [value for value in sentences if value != valueToBeRemoved]
        return sentences
    elif tokenType == "file":
        raise ValueError("To Be Implemented")
    else:
        raise ValueError("Invalid Token Type")

def computeSimilarities(listOfTokens, listOfTokens2): 
    #Encode all sentences
    embeddings1 = model.encode(listOfTokens)
    embeddings2 = model.encode(listOfTokens2)

    #Compute cosine similarity between all pairs
    return util.cos_sim(embeddings1, embeddings2)

def log(customName, similarityValues, sentences1, sentences2, amtOfResultsToLog=10):
    #Add all pairs to a list with their cosine similarity score
    all_sentence_combinations = []
    for i in range(len(similarityValues)-1):
        for j in range(i+1, len(similarityValues[i+1])):
            all_sentence_combinations.append([similarityValues[i][j], i, j])

    #Sort list by the highest cosine similarity score
    all_sentence_combinations = sorted(all_sentence_combinations, key=lambda x: x[0], reverse=True)

    f = open("results/{}.txt".format(customName), 'a')
    for score, i, j in all_sentence_combinations[0:amtOfResultsToLog]:
        f.write("{}\n{}\n{:.4f}\n".format(sentences1[i], sentences2[j], similarityValues[i][j]))
