class Persona:
    __nombre = ''
    __apellido = ''
    __edad = 0
    __profesion = ''
    def __init__ (self, nom= '', app='', ed=0, prof=''):
        self.__nombre = nom
        self.__apellido = app
        self.__edad = ed
        self.__profesion = prof
    def __str__ (self):
        return "%s %s %d %s" %(self.__nombre, self.__apellido, self.__edad, self.__profesion)
    def getNombreApell (self):
        return self.__nombre + self.__apellido
    
    def getNombre(self):
        return self.__nombre
    def getApellido (self):
        return self.__apellido
    def getEdad (self):
        return self.__edad
    def getProfesion (self):
        return self.__profesion
    def mostrarPersona (self):
        print("\nNombre: {} - Apellido: {} - Edad: {} - Profesion: {}".format(self.__nombre, self.__apellido, self.__edad, self.__profesion))
    
    def __gt__ (self, otraPersona):
        if ((type(self)) == (type(otraPersona))):
            return (self.__edad > otraPersona.getEdad())
        elif (type(otraPersona) == int ):
            return (self.__edad > otraPersona)
