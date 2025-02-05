from Model import Antibiotico
from Model import ProductoFertilizante
from Model import ProductoPlaga
from Data.Data import *

class controlProducto:

    @staticmethod
    def agregarAntibiotico(nombre, dosis, tipo, precio):
        antibiotico = Antibiotico.create(nombre, dosis, tipo, precio)
        Data.almacenarProductos(antibiotico)

    @staticmethod
    def agregarFertilizante(ICAFer, nombreFer, frecuenciaFer, precioFer, ultimaFer):
        fertilizante = ProductoFertilizante.ProductoFertilizante.create(ICAFer, nombreFer, frecuenciaFer, ultimaFer, precioFer)
        Data.almacenarProductos(fertilizante)

    def agregarPlaga(ICAPlaga, nombrePlaga,frecuenciaPl,precioPl,carenciaPl):
        plaga = ProductoPlaga.ProductoPlaga.create(ICAPlaga, nombrePlaga,frecuenciaPl,carenciaPl, precioPl)
        Data.almacenarProductos(plaga)
        
    
