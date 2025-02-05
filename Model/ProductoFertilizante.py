from .ProductoControl import ProductoControl

class ProductoFertilizante(ProductoControl):
    def __init__(self, ICA, nombre, frecuencia, ultimaAplicacion, precio):
        self.ultimaAplicacionFertilizante = ultimaAplicacion
        super().__init__(ICA, nombre, frecuencia, precio)

    @property
    def ultimaAplicacionFertilizante(self):
        return self.__ultimaAplicacionFertilizante

    @ultimaAplicacionFertilizante.setter
    def ultimaAplicacionFertilizante(self, ultimaAplicacion):
        self.__ultimaAplicacionFertilizante = ultimaAplicacion


    @staticmethod
    def create(ICAFer, nombreFer, frecuenciaFer, precioFer, ultimaFer):
        return ProductoFertilizante(ICAFer, nombreFer, frecuenciaFer, precioFer, ultimaFer)
    
    def read():
        pass
    
    def relation():
        pass


    def printDataFertilizantes(self):
        print(self.controlICA,self.controlNombre,self.controlFrecuencia,self.controlPrecio, self.ultimaAplicacionFertilizante)