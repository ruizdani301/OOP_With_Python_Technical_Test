from .Nave import Nave

class Lanzadera(Nave):
    def __init__(self, nombre, max_carga, max_distancia):
        super().__init__(nombre)
        self.max_carga = max_carga
        self.max_distancia = max_distancia
               
        
    #def __init__(self, max_carga, peso_actual, carga, empuje, max_distancia, potencia):
    #    self.__max_carga=max_carga
    #    self.__peso_actual=peso_actual
    #    self.__carga= carga
    #    self.__empuje=empuje
    #    self.__max_distancia=max_distancia
    #    self.__potencia=potencia

    def __agregar_carga(self, nombre:str, peso:int)->dict:
        pass
