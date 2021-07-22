from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, time

global width, height, SLIDER_NUM
SLIDER_NUM = 12

class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()

		#Screen Resolution
		x_pos, y_pos = (width//100)*5, (height//100)*5
		self.setGeometry(x_pos, y_pos, (width//100)*95, (height//100)*95)

		#Title & Icon
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.setWindowTitle("StyleGan2")

		self.init_UI()

	def init_UI(self):

		#Items in ComboBox(StyleType) eg Faces, Cars and Abstracts etc.
		x, y = (self.frameGeometry().width())/100, (self.frameGeometry().height())/100
		global SLIDER_NUM
	

		self.styleType = QtWidgets.QComboBox(self)
		self.styleType.setGeometry(QtCore.QRect(x*2.7, y*4.1, x*25, y*4.1))
		self.styleType.addItem("Faces")
		self.styleType.addItem("Other")
		self.styleType.addItem("Another")

		#scrollBox
		self.scrollArea = QtWidgets.QScrollArea(self)
		self.scrollArea.setGeometry(x*2.7, y*13.5, x*25, y*75)
		self.scrollArea.setWidgetResizable(True)
		x_slider, y_slider = (self.scrollArea.frameGeometry().width())/100, (self.scrollArea.frameGeometry().height())/100
		y_container = 1.5

		for i in range(SLIDER_NUM):
			self.sliderContainer = QtWidgets.QWidget(self.scrollArea)
			self.sliderContainer.setStyleSheet("background-color : grey")
			self.sliderContainer.setGeometry(x_slider*2, y_slider*y_container, x_slider*96, y_slider*10)
			y_container += 11.5


		#Random Button7
		self.randomButton = QtWidgets.QPushButton(self)
		self.randomButton.setGeometry(QtCore.QRect(x*6.9, y*91.6, x*16.6, y*4.1))
		self.randomButton.setText("Randomize")
		pass

		#ImageBoxself.imageBox = QtWidgets.QLabel(self)
		self.imageBox = QtWidgets.QLabel(self)
		self.imageBox.setPixmap(QtGui.QPixmap("avatar.jpeg"))
		self.imageBox.setScaledContents(True)
		self.imageBox.setGeometry(x*30.5, y*4.1, x*66.6, y*91.9)


def App():
	global width, height
	app = QApplication(sys.argv)
	screen_resolution = app.desktop().screenGeometry()
	width, height = screen_resolution.width(), screen_resolution.height()
	win = Window()
	win.show()
	sys.exit(app.exec_())
	print(SLIDER_NUM)

App()