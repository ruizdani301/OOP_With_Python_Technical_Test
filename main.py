from src.Nave import Nave
from src.Tripulado import Tripulado
from src.No_tripulado import No_tripulado
from src.Lanzadera import Lanzadera
class Main:

    #def crear_nave(self, nombre:str, tipo_nave: str, peso:float, velocidad:float, tamaño:float, proposito:str, cantidad_conbustible:float, tipo_conbustible:str, año_origem:int, pais_fabricante:str):
    #    pass
    listanave = []

    def crear_nave(self, tipo:str, **k):
        if tipo == "Nave":
            nave1 = Nave(k["nombre"])

        elif tipo == "Lanzadera":
            print(k)
            nave1 = Lanzadera(k["nombre"], k["max_carga"], k["max_distancia"])

        elif tipo == "No_tripulado":
            nave1 = No_tripulado(k["nombre"],k["energia_alternativa"],k["empuje"])

        elif tipo == "Tripulado":
            nave1 = Tripulado(k["nombre"], k["capacidad"])
        
        else:
            print("ingresa un tipo")
            return
        self.listanave.append(nave1)
        

    def buscar_nave(self, tipo:Nave)->list[Nave]:
        pass

    def mostrar_nave(self, tipo:str)->list[Nave]:
        for i in self.listanave:
            print(i.nombre)

    
if __name__=="__main__":
    main = Main()
    inicio = True
    dicc = {}
    #lanza = Lanzadera("maria",4)
    #print(lanza)
    menu1 = {"1": "Nave", "2":"Tripulado", "3":"No_tripulado", "4":"Lanzadera"}
    while inicio:
        print("seleccione una nave")
        for k,v in menu1.items():
            print(f'{k}:{v}')
        seleccion = input("seleccione una nave: ")

        match seleccion:
            case "1":
                nombre= input("escriba el nombre de la nave: " )
                dicc = {"nombre": nombre}

            case "2":
                nombre= input("escriba el nombre de la nave: " )
                tripulantes= input("escriba cantidad maxima de tripulantes: " )
                dicc = {"nombre": nombre, "capacidad":tripulantes }
                
            case "3":
                nombre= input("Escriba el nombre de la nave: ")
                energia= input("Energia alternativa: ")
                empuje= input("Escriba el empuje: ")
                dicc = {"energia_alternativa":energia, "empuje":empuje}
        
            case "4":
                nombre = input("Escriba el nombre de la nave: ")
                max_carga = input("Escriba el maximo peso de carga entoneladas: ")
                max_distancia = input("Escriba la distancia maxima de recorrido: ")
                dicc = {"nombre":nombre, "max_carga":max_carga, "max_distancia":max_distancia}


        print("\n--------------\n")    
        main.crear_nave(menu1[seleccion], **dicc)
        main.mostrar_nave("Nave")

          
