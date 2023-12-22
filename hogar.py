class Hogar():
    def __init__(self):
        self._tipo = ''
        self._jardin = False
        self._terraza = False

    def get_tipo(self):
        return self._tipo
         
    def set_tipo(self, tipo):
        self._tipo = tipo
    
    def get_jardin(self):
        return self._jardin
         
    def set_jardin(self, jardin):
        self._jardin = jardin
    
    def get_terraza(self):
        return self._terraza
         
    def set_terraza(self, terraza):
        self._terraza = terraza

    def __str__(self): 
        return "{ Hogar: Tipo: % s; Jardin: % s; Terraza: % s; }" \
        % (self._tipo, self._jardin, self._terraza)