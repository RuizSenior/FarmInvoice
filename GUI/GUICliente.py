from Controller import ControllerCliente
from PyQt5.QtWidgets import *
from Data.Data import *
from PySide2.QtWidgets import *




class QtCliente:

    def guiAñadirCliente(self):
        nombre = self.nombre.text()
        cedula = self.cedula.text()

        msg = QMessageBox()

        if (nombre == "" or cedula == ""):
            msg.setWindowTitle("Error")
            msg.setText("Error")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setInformativeText("Por favor rellene todos los espacios")

            x = msg.exec_()

        else:
            msg.setWindowTitle("Exito")
            msg.setText("Exito")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setInformativeText("El cliente fue agregado de forma exitosa")
             
            x = msg.exec_()
            ControllerCliente.controlCliente.agregarCliente(cedula,nombre)
            self.cargarTablaClientes(nombre, cedula)

            self.nombre.clear()
            self.cedula.clear()


        print("-------------")

    def guiEliminarCliente(self):
        cedula = self.cedulaEli.text()

        msg = QMessageBox()

        if (cedula == ""):
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
                msg.setWindowTitle("Exito")
                msg.setText("Exito")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setInformativeText("El cliente fue eliminado de forma exitosa")
                
                x = msg.exec_()
                ControllerCliente.controlCliente.eliminarCliente(cedula)
                self.eliminarTablaClientes(Data.clientes)
                self.cedulaEli.clear()           

        print("-------------")

    def cargarTablaClientes(self, nombre, cedula):
        row = self.tablaClientes.rowCount()
        self.tablaClientes.insertRow(row)
        self.tablaClientes.setItem(row, 0, QTableWidgetItem(cedula))
        self.tablaClientes.setItem(row, 1, QTableWidgetItem(nombre))

    def eliminarTablaClientes(self, clientes):
        self.tablaClientes.setRowCount(0)

        for cedula, value in clientes.items():
            row = self.tablaClientes.rowCount()
            self.tablaClientes.insertRow(row)
            self.tablaClientes.setItem(row, 0, QTableWidgetItem(cedula))
            self.tablaClientes.setItem(row, 1, QTableWidgetItem(value.nombre))





        print("-------------")