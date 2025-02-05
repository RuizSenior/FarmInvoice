from Controller import ControllerFactura
from PyQt5.QtWidgets import *
from Data.Data import *
from PySide2.QtWidgets import *

class QtFactura:

    def guiCrearFactura(self):
        nombreProductoComprar = self.nombreProComprar.text()
        fecha = self.fechaFactura.text()
        cedula = self.facturaCliente.text()

        msg = QMessageBox()

        if( nombreProductoComprar == "" or fecha == "" or cedula == ""):
            msg.setWindowTitle("Error")
            msg.setText("Error")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setInformativeText("Por favor rellene todos los espacios")

            x = msg.exec_()

        else:
            if cedula not in Data.clientes or nombreProductoComprar not in Data.productos:
                msg.setWindowTitle("Error")
                msg.setText("Error")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setInformativeText("El cliente o producto no esta en la base de datos")
                x = msg.exec_()

            else:
                msg.setWindowTitle("Exito")
                msg.setText("Exito")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setInformativeText("La factura se creo de forma exitosa")
                x = msg.exec_()
                ControllerFactura.controlFactura.crearFactura(nombreProductoComprar,fecha,cedula)

                self.nombreProComprar.clear()
                self.fechaFactura.clear()
                self.facturaCliente.clear()


    def guiMostrarFacturasCliente(self):

        self.tablaFacturas.setRowCount(0)
        self.precioTotal.setText("")
        cedula = self.cedulaMostrarFacturas.text()

        msg = QMessageBox()

        if( cedula == "" ):
            msg.setWindowTitle("Error")
            msg.setText("Error")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setInformativeText("Por favor rellene todos los espacios")

            x = msg.exec_()

        else:
            if cedula not in Data.clientes:
                msg.setWindowTitle("Error")
                msg.setText("Error")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setInformativeText("El cliente no esta en la base de datos")

                x = msg.exec_()

            else:
                facturasCliente = Data.clientes[cedula]

                valorTotal = 0

                for index in facturasCliente.facturas:
                    row = self.tablaFacturas.rowCount()
                    self.tablaFacturas.insertRow(row)
                    self.tablaFacturas.setItem(row, 0, QTableWidgetItem(index.fechaFactura))
                    self.tablaFacturas.setItem(row, 1, QTableWidgetItem(index.precioFactura))
                    self.tablaFacturas.setItem(row, 2, QTableWidgetItem(index.nombreProductoFactura))

                    valorTotal += int(index.precioFactura)

                    

                self.precioTotal.setText(str(valorTotal))
                self.cedulaMostrarFacturas.clear()


        
            