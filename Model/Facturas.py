from Interfaces import ICrud


class Facturas(ICrud.ICrud):
    def __init__(self, fecha, precio, nombreProducto):
        self.__fechaFactura = fecha
        self.__precioFactura = precio
        self.__nombreProductoFactura = nombreProducto

    @property
    def fechaFactura(self):
        return self.__fechaFactura

    @fechaFactura.setter
    def fechaFactura(self, fecha):
        self.__fechaFactura = fecha

    @property
    def precioFactura(self):
        return self.__precioFactura

    @precioFactura.setter
    def precioFactura(self, precio):
        self.__precioFactura = precio

    @property
    def nombreProductoFactura(self):
        return self.__nombreProductoFactura

    @nombreProductoFactura.setter
    def nombreProductoFactura(self, nombreProducto):
        self.__nombreProductoFactura = nombreProducto

    @staticmethod
    def create(fecha, precio, nombreProducto):
        return Facturas(fecha, precio, nombreProducto)
    
    def read():
        pass
    
    def relation():
        pass


        '''
    def printDataFactura(self):
        print("{:^10}, {:^10}, {:^10}".format(self.fechaFactura,self.precioFactura,self.nombreProductoFactura))
        '''