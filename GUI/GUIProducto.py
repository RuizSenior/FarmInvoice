from Controller import ControllerProducto
from PyQt5.QtWidgets import *
from Data.Data import *
from PySide2.QtWidgets import *

class QtProducto:

    def guiAñadirAntibiotico(self):
        nombre = self.nombreAntibiotico.text()
        dosis = self.dosisAntibiotico.text()
        animal = self.tipoAnimal.currentText()
        precio = self.precioAntibiotico.text()

        msg = QMessageBox()

        if (nombre == "" or dosis == "" or animal == "" or precio == ""):
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
            msg.setInformativeText("El antibiotico fue agregado de forma exitosa")
            x = msg.exec_()

            ControllerProducto.controlProducto.agregarAntibiotico(nombre,dosis,animal,precio)

            self.cargarTablaAntibioticos(nombre,dosis,animal,precio)

            self.nombreAntibiotico.clear()
            self.dosisAntibiotico.clear()
            self.tipoAnimal.setCurrentIndex(0)
            self.precioAntibiotico.clear()

        


    def cargarTablaAntibioticos(self, nombre, dosis, animal, precio):
        row = self.tablaAntibioticos.rowCount()
        self.tablaAntibioticos.insertRow(row)
        self.tablaAntibioticos.setItem(row, 0, QTableWidgetItem(nombre))
        self.tablaAntibioticos.setItem(row, 1, QTableWidgetItem(dosis))
        self.tablaAntibioticos.setItem(row, 2, QTableWidgetItem(animal))
        self.tablaAntibioticos.setItem(row, 3, QTableWidgetItem(precio))


    def guiAñadirFertilizante(self):
        ICAFer = self.ICAFertilizante.text()
        nombreFer = self.nombreFertilizante.text()
        frecuenciaFer = self.frecuenciaFertilizante.text()
        precioFer = self.precioFertilizante.text()
        ultimaFer = self.ultimaApliFertilizante.text()

        msg = QMessageBox()

        if (ICAFer == "" or nombreFer == "" or frecuenciaFer == "" or precioFer == "" or ultimaFer == ""):
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
            msg.setInformativeText("El fertilizante fue agregado de forma exitosa")
            x = msg.exec_()

            ControllerProducto.controlProducto.agregarFertilizante(ICAFer, nombreFer, frecuenciaFer, precioFer, ultimaFer)
            self.cargarTablaFertilizantes(ICAFer, nombreFer, frecuenciaFer, ultimaFer, precioFer,)

            self.ICAFertilizante.clear()
            self.nombreFertilizante.clear()
            self.frecuenciaFertilizante.clear()
            self.precioFertilizante.clear()
            self.ultimaApliFertilizante.clear()



    def cargarTablaFertilizantes(self, ICAFer, nombreFer, frecuenciaFer, precioFer, ultimaFer):
        row = self.tablaFertilizante.rowCount()
        self.tablaFertilizante.insertRow(row)
        self.tablaFertilizante.setItem(row, 0, QTableWidgetItem(ICAFer))
        self.tablaFertilizante.setItem(row, 1, QTableWidgetItem(nombreFer))
        self.tablaFertilizante.setItem(row, 2, QTableWidgetItem(frecuenciaFer))
        self.tablaFertilizante.setItem(row, 3, QTableWidgetItem(precioFer))
        self.tablaFertilizante.setItem(row, 4, QTableWidgetItem(ultimaFer))




    def guiAñadirPlaga(self):
        ICAPlaga = self.ICAPlagas.text()
        nombrePlaga = self.nombrePlaga.text()
        frecuenciaPl = self.frecuenciaPlaga.text()
        precioPl = self.precioPlaga.text()
        carenciaPl = self.carenciaPlaga.text()


        msg = QMessageBox()

        if (ICAPlaga == "" or nombrePlaga == "" or frecuenciaPl == "" or precioPl == "" or carenciaPl == ""):
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
            msg.setInformativeText("El cotrol de plagas fue agregado de forma exitosa")
            x = msg.exec_()
            
            ControllerProducto.controlProducto.agregarPlaga(ICAPlaga, nombrePlaga,frecuenciaPl,precioPl,carenciaPl)
            self.cargarTablaPlagas(ICAPlaga, nombrePlaga,frecuenciaPl,precioPl,carenciaPl)

            self.ICAPlagas.clear()
            self.nombrePlaga.clear()
            self.frecuenciaPlaga.clear()
            self.precioPlaga.clear()
            self.carenciaPlaga.clear()



    def cargarTablaPlagas(self, ICAPlaga, nombrePlaga,frecuenciaPl,precioPl,carenciaPl):
        row = self.tablaPlagas.rowCount()
        self.tablaPlagas.insertRow(row)
        self.tablaPlagas.setItem(row, 0, QTableWidgetItem(ICAPlaga))
        self.tablaPlagas.setItem(row, 1, QTableWidgetItem(nombrePlaga))
        self.tablaPlagas.setItem(row, 2, QTableWidgetItem(frecuenciaPl))
        self.tablaPlagas.setItem(row, 4, QTableWidgetItem(precioPl))
        self.tablaPlagas.setItem(row, 3, QTableWidgetItem(carenciaPl))