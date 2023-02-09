from .Nave import Nave

class Tripulado(Nave):
    def __init__(self, nombre, capacidad):
        super().__init__(nombre)
        self.__capacidad=capacidad
        
        

    def agregar_tripulante(self, name:str)->list[str]:
        pass