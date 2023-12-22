from nltk.util import pr
import requests
import json
from nltk.corpus import wordnet
import nltk
from requests.api import get

apikey = "e4bfbfaa-af73-4396-b941-371927a97b72"

def getSynonyms(word):
    url = "https://www.dictionaryapi.com/api/v3/references/thesaurus/json/" + word + "?key=" + apikey

    response = requests.get(url)

    data = json.loads(response.text)

    if (type(data[0]) == str):
        return []

    syns = data[0]["meta"]['syns'][0]

    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
             syns.append(lm.name())

    return list(set(syns))
