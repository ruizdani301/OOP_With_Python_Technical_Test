from abc import ABC, abstractmethod

class   Internave(ABC):
    
    @abstractmethod
    def descripccion(self, descriptccion:str)->str:
        pass


    @abstractmethod
    def estado_vuelo(self, estado:str)->str:
        pass
    
    @abstractmethod
    def chequeo(self)-> str:
        pass