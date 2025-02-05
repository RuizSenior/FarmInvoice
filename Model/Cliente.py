from Interfaces import ICrud

class Cliente(ICrud.ICrud):

    def __init__(self, cedula, nombre):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__facturas = list()

    @property
    def nombre(self):
        return self.__nombre
  
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def cedula(self):
        return self.__cedula
  
    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula

    @property
    def facturas(self):
        return self.__facturas
  
    @facturas.setter
    def facturas(self, factura):
        self.__facturas.append(factura)




    def asociarFactura(self, factura):
        self.facturas.append(factura)


    

    
    @staticmethod
    def create(cedula, nombre):
        return Cliente(cedula, nombre)
    
    def read():
        pass
    
    def relation():
        pass





    def printDataCliente(self):
        print(self.cedula,self.nombre)