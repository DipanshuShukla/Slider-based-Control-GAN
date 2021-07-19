from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, time

global width, height

class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		x_pos, y_pos = (width//100)*5, (height//100)*5

		self.setGeometry(x_pos, y_pos, (width//100)*95, (height//100)*95)
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.setWindowTitle("StyleGan2")

		self.init_UI()

	def init_UI(self):
		self.centralwidget = QtWidgets.QWidget(self)
		
		#Items in StyleType eg Faces, Cars and Abstracts etc.

		self.styleType = QtWidgets.QComboBox(self.centralwidget)
		self.styleType.setGeometry(QtCore.QRect(20, 20, 180, 20))
		
		self.styleType.addItem("Faces")
		self.styleType.addItem("Other")
		self.styleType.addItem("Another")
		
def App():
	global width, height
	app = QApplication(sys.argv)
	screen_resolution = app.desktop().screenGeometry()
	width, height = screen_resolution.width(), screen_resolution.height()
	win = Window()
	win.show()
	sys.exit(app.exec_())

App()