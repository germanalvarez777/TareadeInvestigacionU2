from clasePersona import Persona
class ManejadorPersona:
    __listaP = []
    def __init__ (self):
        self.__listaP = []
    def agregarPersona (self, unaPersona):
        self.__listaP.append(unaPersona)
    
    #Se crean las instancias persona, en este caso desde teclado, pero puede ser por archivo csv
 
    def testListaPersona (self):
        otraPersona = Persona ('Julian', 'Fernandez', 33, 'Abogado')
        unaPersona = Persona('Roberto', 'Sanchez', 44, 'Informatico')
        personaX = Persona ('Alvaro', 'Gimenez', 37, 'Docente')
        perY = Persona ('Juan', 'Martin', 19, 'Estudiante')
        personaX2 = Persona ('Manuel', 'Ortega', 25, 'El mejor docente')
        self.agregarPersona(unaPersona)
        self.agregarPersona(otraPersona)
        self.agregarPersona(perY)
        print("Se aplica algunos metodos de Lista" .center(40, "-"))
        self.__listaP.insert (1,personaX)
        print("\nValor de index de Persona Julian: ", self.__listaP.index (otraPersona))
        print("\nSe elimina la Persona Roberto que se encuentra en la primera posicion de la lista\n")
        self.__listaP.pop(0)
        print("Se usa el metodo Extend, añadiendo a persona Roberto y Manuel")
        self.__listaP.extend([unaPersona, personaX2])             #se coloca entre corchetes, pues es iterable
        print("Se ordena la lista por sort: ")
        self.__listaP.sort()

    def mostrarListaPersona (self):
        for pers in self.__listaP:
            print("".center(50, '='))
            pers.mostrarPersona()
