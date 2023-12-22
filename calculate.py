from filemanager import *
from dictionary import *
from persona import *
from dog import *
from synonyms import * 
import operator

#Read data from json
razas = readJson()
pesoGrande = 25
alturaGrande = 40
pesoPequeño = 15
alturaPequeño = 30

def recomendedDog(persona: Persona) -> Dog:
    for raza in razas:
        raza.compatibility = 0
        if persona.get_hogar().get_tipo == "house":
            if not persona.get_hogar().get_jardin:
                if (raza.weight > pesoPequeño and raza.weight < pesoGrande) and (raza.height > alturaPequeño and raza.height < alturaGrande):
                    raza.compatibility += 1
                elif  raza.weight > pesoGrande or raza.height > alturaGrande:
                    raza.compatibility += 0.75
                elif raza.weight < pesoPequeño or raza.height < alturaPequeño:
                    raza.compatibility += 0.75
            else:
                if (raza.weight > pesoPequeño and raza.weight < pesoGrande) and (raza.height > alturaPequeño and raza.height < alturaGrande):
                    raza.compatibility += 0.75
                elif  raza.weight > pesoGrande or raza.height > alturaGrande:
                    raza.compatibility += 1
                elif raza.weight < pesoPequeño or raza.height < alturaPequeño:
                    raza.compatibility += 0.5
        elif persona.get_hogar().get_tipo() == "apartment":
            if not persona.get_hogar().get_terraza:
                if (raza.weight > pesoPequeño and raza.weight < pesoGrande) and (raza.height > alturaPequeño and raza.height < alturaGrande):
                    raza.compatibility += 0.75
                elif raza.weight < pesoPequeño or raza.height < alturaPequeño:
                    raza.compatibility += 1
            else:
                if (raza.weight > pesoPequeño and raza.weight < pesoGrande) and (raza.height > alturaPequeño and raza.height < alturaGrande):
                    raza.compatibility += 1
                elif  raza.weight > pesoGrande or raza.height > alturaGrande:
                    raza.compatibility += 0.5
                elif raza.weight < pesoPequeño or raza.height < alturaPequeño:
                    raza.compatibility += 0.75
        if persona.get_tamaño() == "L" and (raza.weight > pesoGrande or raza.height > alturaGrande):
            raza.compatibility += 0.7
        elif persona.get_tamaño() == "M" and (raza.weight > pesoPequeño and raza.weight < pesoGrande) and (raza.height > alturaPequeño and raza.height < alturaGrande):
            raza.compatibility += 0.7
        elif persona.get_tamaño() == "S" and (raza.weight < pesoPequeño or raza.height < alturaPequeño):
            raza.compatibility += 0.7
    
        for adj in raza.temperament:
            valor = 1 / len(raza.temperament)
            if adj in filtro["hours"] and persona.get_horas() > 5:
                raza.compatibility += float(valor*1.5)
            if adj in filtro["childrens"] and persona.get_niños():
                raza.compatibility += float(valor*1.3)
            if adj in filtro["disability"] and persona.get_discapacidad():
                raza.compatibility += float(valor*1.5)
                if persona.get_finalidad() == "disability":
                    raza.compatibility += float(valor*1.5)
            if adj in filtro["pets"] and persona.get_mascotas():
                raza.compatibility += float(valor*1.3)
            if adj in filtro["sports"] and persona.get_deporte():
                raza.compatibility += float(valor*1.2)
            if adj in persona.get_caracter():
                raza.compatibility += float(valor)      
        
        if persona.get_finalidad() != "disability":
            for finalidad in dog_for[persona.get_finalidad()]:
                if finalidad in raza.bredFor:
                    raza.compatibility += 1
        else:
            if raza.name in dog_for[persona.get_finalidad()]:
                raza.compatibility += 1

        frase = persona.get_finalidad().lower().split()
        for palabra in frase:
            especialidad = raza.bredFor.lower()
            if especialidad.find(palabra.lower()) > -1:
                raza.compatibility += 0.5

        raza.compatibility = round(raza.compatibility,2)
    razas.sort(key=operator.attrgetter("compatibility"),reverse=True)

    print(razas[0])
    print(razas[1])
    print(razas[2])
    print(razas[3])
    print(razas[4])
    print(razas[5])
    print(razas[6])
    print(razas[7])

    return razas[0]

