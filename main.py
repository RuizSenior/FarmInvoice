
import sys, os
from GUI.EstablecerVentana import *
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from Controller.ControllerCliente import *



class MiApp(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)



		#eliminar barra y de titulo - opacidad
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		#SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

		# mover ventana
		self.ui.frame_Superior.mouseMoveEvent = self.mover_ventana

		#acceder a las paginas
		self.ui.lateralAgregarCliente.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cliente))			
		self.ui.lateralMostrarCliente.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.MostrarCli))
		self.ui.lateralAgregarProducto.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Producto))	
		self.ui.lateralMostrarProducto.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.MostrarPro))
		self.ui.lateralFacturas.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Facturas))	

		self.ui.btAntibiotico.clicked.connect(lambda: self.ui.stackedWidgetPro.setCurrentWidget(self.ui.pgAntibiotico))
		self.ui.btFertilizante.clicked.connect(lambda: self.ui.stackedWidgetPro.setCurrentWidget(self.ui.pgFertilizante))
		self.ui.btPlagas.clicked.connect(lambda: self.ui.stackedWidgetPro.setCurrentWidget(self.ui.pgPlagas))

		

		#control barra de titulos
		self.ui.minimizar.clicked.connect(self.control_bt_minimizar)		
		self.ui.restaurar.clicked.connect(self.control_bt_normal)
		self.ui.maximizar.clicked.connect(self.control_bt_maximizar)
		self.ui.cerrar.clicked.connect(lambda: self.close())

		self.ui.restaurar.hide()



		#Botoenes agregar
		self.ui.btAgregarCliente.clicked.connect(self.ui.guiAñadirCliente)
		self.ui.btEliminar.clicked.connect(self.ui.guiEliminarCliente)
		self.ui.btAgregarPro.clicked.connect(self.ui.guiAñadirAntibiotico)
		self.ui.btAgregarFer.clicked.connect(self.ui.guiAñadirFertilizante)
		self.ui.btAgregarPlaga.clicked.connect(self.ui.guiAñadirPlaga)
		self.ui.btCrearFactura.clicked.connect(self.ui.guiCrearFactura)
		self.ui.btMostraFactura.clicked.connect(self.ui.guiMostrarFacturasCliente)

        




	def control_bt_minimizar(self):
		self.showMinimized()		

	def  control_bt_normal(self): 
		self.showNormal()		
		self.ui.restaurar.hide()
		self.ui.maximizar.show()

	def  control_bt_maximizar(self): 
		self.showMaximized()
		self.ui.maximizar.hide()
		self.ui.restaurar.show()

	def mover_menu(self):
		if True:			
			width = self.ui.frame_lateral.width()
			normal = 0
			if width==0:
				extender = 200
			else:
				extender = normal
			self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()

	## SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

	## mover ventana
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()

	def mover_ventana(self, event):
		if self.isMaximized() == False:			
			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()

		if event.globalPos().y() <=20:
			self.showMaximized()
		else:
			self.showNormal()




	




if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	


'''
def menu():
    op = int(input("Opcion: "))

    if op == 1:
        cedula = int(input("Cedula: "))
        nombre = input("Nombre: ")
        ControllerCliente.controlCliente.agregarCliente(cedula,nombre)

    if op == 2:
        cedula = int(input("Cedula a eliminar: "))
        ControllerCliente.controlCliente.eliminarCliente(cedula)

    

    menu()

'''

        
