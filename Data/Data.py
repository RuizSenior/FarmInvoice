from Model.Cliente import Cliente
from Model.Antibiotico import Antibiotico
from Model.Facturas import Facturas


class Data(object):
    clientes = {} #{cedula: client}
    productos = {}



    @staticmethod
    def save_client(client):      
        Data.clientes.update({client.cedula: client})
      
        for index in Data.clientes.values():
            index.printDataCliente()
        
    
    @staticmethod
    def delete_client(cedula):
        
        if(cedula not in Data.clientes):
            print("Error, el cliente no ha sido creado")

        Data.clientes.pop(cedula)

        for index in Data.clientes.values():
            index.printDataCliente()


    @staticmethod
    def almacenarProductos(producto):      
        Data.productos.update({producto.nombre: producto})
              
        '''
        for index in Data.productos.values():

            if type(index) == Antibiotico:
                index.printDataAntibioticos()
        
'''

    @staticmethod
    def asociarFacturaCliente(factura,cedula):

        cliente = Data.clientes[cedula]
        cliente.asociarFactura(factura)

        facturasCliente = Data.clientes[cedula]

        '''
        for index in facturasCliente.facturas:
            index.printDataFactura()

            '''