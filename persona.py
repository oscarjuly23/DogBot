from animal import Animal
from hogar import Hogar

class Persona(Animal):
    def __init__(self):
        self._caracter = []
        Animal.__init__(self,self._caracter)
        self._edad = 0
        self._finalidad = ''
        self._niños = False
        self._tamaño = ''
        self._horas = 0
        self._deporte = False
        self._discapacidad = False
        self._mascotas = False
        self._hogar = Hogar()
        
    def get_edad(self):
        return self._edad
         
    def set_edad(self, edad):
        self._edad = edad
        
    def get_caracter(self):
        return self._caracter
         
    def set_caracter(self, caracter):
        self._caracter = caracter
         
    def get_finalidad(self):
        return self._finalidad
         
    def set_finalidad(self, finalidad):
        self._finalidad = finalidad
    
    def get_niños(self):
        return self._niños
         
    def set_niños(self, niños):
        self._niños = niños
        
    def get_tamaño(self):
        return self._tamaño
         
    def set_tamaño(self, tamaño):
        self._tamaño = tamaño
        
    def get_horas(self):
        return int(self._horas)
         
    def set_horas(self, horas):
        self._horas = horas
        
    def get_deporte(self):
        return self._deporte
         
    def set_deporte(self, deporte):
        self._deporte = deporte
        
    def get_discapacidad(self):
        return self._discapacidad
         
    def set_discapacidad(self, discapacidad):
        self._discapacidad = discapacidad
        
    def get_mascotas(self):
        return self._mascotas
         
    def set_mascotas(self, mascotas):
        self._mascotas = mascotas
        
    def get_hogar(self):
        return self._hogar
         
    def set_hogar(self, hogar):
        self._hogar = hogar

    def __str__(self): 
        return "{ Persona: Edad: % s; Finalidad: % s; Niños: % s; Tamaño: % s; Horas: % s; Deporte: % s; Discapacidad: % s; Mascotas: % s; Caracter: % s; Hogar: % s; }" \
        % (self._edad, self._finalidad, self._niños, self._tamaño, self._horas, self._deporte, self._discapacidad, self._mascotas, self._caracter, self._hogar) 