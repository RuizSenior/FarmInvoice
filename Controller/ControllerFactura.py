from Model.Facturas import *
from Data.Data import *
from Model.Cliente import *

class controlFactura:


    @staticmethod
    def crearFactura(nombreProductoComprar,fecha,cedula):

        producto = Data.productos[nombreProductoComprar]
        factura = Facturas.create(fecha, producto.precio, producto.nombre)

        Data.asociarFacturaCliente(factura, cedula)

        #factura.printDataFactura()

        
        