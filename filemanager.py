import json
from dog import *

def readJson():
    dogs = []
    f = open('data.json', encoding='utf-8')
    data = json.load(f)

    for i in data:
        c = i['temperament'].lower().split()
        caracter = []
        for j in c:
            caracter.append(j)
        height = i['height']['metric'].split(' - ')
        if len(height) > 1:
            altura = (float) (int(height[0]) + int(height[1])) / 2
        else: 
            altura = int(height[0])
        weight = i['weight']['metric'].split(' - ')
        if len(weight) > 1:
            peso = (float) (int(weight[0]) + int(weight[1])) / 2
        else: 
            peso = int(weight[0])
        dog = Dog(i.get('bred_for','').lower(),i['name'],altura,peso,i['image']['url'],caracter)
        dogs.append(dog)
    f.close()

    return dogs

def breedExists(text):
    dogExist = None
    dogs = readJson()

    for i in dogs:
        if i.name.lower() in text.lower():
            dogExist = i

    return dogExist
