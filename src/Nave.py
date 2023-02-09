from .Internave import Internave

class Nave(Internave):
    def __init__(self, nombre):
        self.nombre=nombre
    """
    def __init__(self, nombre,peso,velocidad,tamaño,proposito,cantidad_conbustible, tipo_conbustible, año_origen, año_retiro, pais_fabricante):
        self.__nombre=nombre
        self.__peso=peso
        self.__velocidad=velocidad
        self.__tamaño=tamaño
        self.__proposito=proposito
        self.__cantidad_conbustible=cantidad_conbustible
        self.__tipo_conbustible=tipo_conbustible
        self.__año_origen=año_origen
        self.__año_retiro=año_retiro
        self.__pais_fabricante=pais_fabricante

    """
    def nivel_conbustible()-> int:
        pass

    def descripccion(self, descriptccion:str)->str:
        pass


    def estado_vuelo(self, estado:str)->str:
        pass
    
    def chequeo(self)-> str:
        pass
