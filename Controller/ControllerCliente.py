from Model import Cliente
from Data.Data import *

class controlCliente:

    @staticmethod
    def agregarCliente(cedula, nombre):
        client = Cliente.create(cedula, nombre)
        Data.save_client(client)
    
    @staticmethod
    def eliminarCliente(cedula):
        Data.delete_client(cedula)