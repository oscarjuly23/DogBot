class Dog():
    def __init__(self, bredFor, name, height, weight, image, temperament):
        self.bredFor = bredFor
        self.name = name
        self.height = height
        self.weight = weight
        self.image = image
        self.temperament = temperament
        self.compatibility = 0

    def __str__(self): 
        return "{ Dog: Especialidad: % s; Raza: % s; Altura: % d; Peso: % d; Foto: % s; Caracter: % s; Compatibilidad: % s;}" \
        % (self.bredFor, self.name, self.height, self.weight, self.image, self.temperament, self.compatibility) 