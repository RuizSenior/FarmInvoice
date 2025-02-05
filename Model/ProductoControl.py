from Interfaces import ICrud

class ProductoControl(ICrud.ICrud):

    def __init__(self,ICA, nombre, frecuencia, precio):
        self.__nombre = nombre
        self.__controlFrecuencia = frecuencia
        self.__precio = precio
        self.__controlICA = ICA

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def controlFrecuencia(self):
        return self.__controlFrecuencia

    @controlFrecuencia.setter
    def controlFrecuencia(self, frecuencia):
        self.__controlFrecuencia = frecuencia

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def controlPrecio(self, precio):
        self.__precio = precio

    @property
    def controlICA(self):
        return self.__controlICA

    @controlICA.setter
    def controlICA(self, ICA):
        self.__controlICA = ICA

    @staticmethod
    def create(ICA, nombre, frecuencia, precio):
        return ProductoControl(ICA, nombre, frecuencia, precio)
    
    def read():
        pass
    
    def relation():
        pass