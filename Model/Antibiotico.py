from Interfaces import ICrud

class Antibiotico(ICrud.ICrud):
    def __init__(self, nombreProducto, dosis, tipoAnimal, precio):
        self.__antibioticoNombre = nombreProducto
        self.__antibioticoDosis = dosis
        self.__antibioticoAnimal = tipoAnimal
        self.__precio = precio

    @property
    def antibioticoNombre(self):
        return self.__antibioticoNombre
  
    @antibioticoNombre.setter
    def nombre(self, nombreProducto):
        self.__antibioticoNombre = nombreProducto
    
    @property
    def antibioticoDosis(self):
        return self.__antibioticoDosis
  
    @antibioticoDosis.setter
    def cedula(self, dosis):
        self.__antibioticoDosis = dosis

    @property
    def antibioticoAnimal(self):
        return self.__antibioticoAnimal

    @antibioticoAnimal.setter
    def antibioticoAnimal(self, tipoAnimal):
        self.__antibioticoAnimal = tipoAnimal

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def antibioticoPrecio(self, precio):
        self.__precio = precio


    @staticmethod
    def create(nombreProducto, dosis, tipoAnimal, precio):
        return Antibiotico(nombreProducto, dosis, tipoAnimal, precio)
    
    def read():
        pass
    
    def relation():
        pass




    def printDataAntibioticos(self):
        print(self.antibioticoNombre,self.antibioticoDosis,self.antibioticoAnimal,self.antiboticoPrecio)
   
