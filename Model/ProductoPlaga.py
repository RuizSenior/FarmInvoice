from .ProductoControl import ProductoControl

class ProductoPlaga(ProductoControl):
    def __init__(self, ICA, nombre, frecuencia, carencia, precio):
        self.carenciaPlaga = carencia
        super().__init__(ICA, nombre, frecuencia, precio)

    @property
    def carenciaPlaga(self):
        return self.__carenciaPlaga

    @carenciaPlaga.setter
    def carenciaPlaga(self, carencia):
        self.__carenciaPlaga = carencia

    @staticmethod
    def create(ICAPlaga, nombrePlaga,frecuenciaPl,precioPl,carenciaPl):
        return ProductoPlaga(ICAPlaga, nombrePlaga,frecuenciaPl,precioPl,carenciaPl)
    
    def read():
        pass
    
    def relation():
        pass





    def printDataPlagas(self):
        print(self.controlICA,self.controlNombre,self.controlFrecuencia,self.controlPrecio, self.carenciaPlaga)