from .Nave import Nave

class No_tripulado(Nave):
    def __init__(self, nombre, energia_alternativa, empuje):
       
        super().__init__(nombre)
        self.__energia_alternativa=energia_alternativa
        self.__empuje=empuje
        
            

    def nivel_energia()->int:
        pass

    def ubicacion_actual()->int:
        pass