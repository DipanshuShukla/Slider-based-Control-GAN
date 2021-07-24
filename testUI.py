from PyQt5 import QtCore, QtGui, QtWidgets
import random

global SLIDER_NUM

#test

SLIDER_NUM = {'1': 10,'2': 10,'3': 10,'4': 10,'5': 10,'6': 10,'7': 10,'8': 10,'9': 10,'10': 10,'11': 10,'12': 10}

class Ui_Window(object):

	def setupUi(self, Window):

		"/////////// ROOT-WONDOW ///////////"

		Window.setObjectName("Window")
		Window.resize(622, 446)
		Window.setWindowIcon(QtGui.QIcon('icon.png'))
		Window.setWindowTitle("StyleGan2")
		Window.setMinimumSize(QtCore.QSize(622, 446))
		Window.setSizeIncrement(QtCore.QSize(-8672, 0))

		self.rootContainer = QtWidgets.QWidget(Window)
		self.rootContainer.setObjectName("rootContainer")
		
		self.gridLayout_2 = QtWidgets.QGridLayout(self.rootContainer)
		self.gridLayout_2.setObjectName("gridLayout_2")
		

		"/////////// BUTTONS ///////////"
		
		self.buttonsContainer = QtWidgets.QHBoxLayout()
		self.buttonsContainer.setObjectName("buttonsContainer")
		
		#random
		self.randomButtonContainer = QtWidgets.QVBoxLayout()
		self.randomButtonContainer.setObjectName("randomButtonContainer")
		self.randomButton = QtWidgets.QPushButton(self.rootContainer)
		self.randomButton.setMinimumSize(QtCore.QSize(0, 20))
		self.randomButton.setObjectName("randomButton")
		self.randomButton.clicked.connect(self.randomize)
		self.randomButtonContainer.addWidget(self.randomButton)
		self.buttonsContainer.addLayout(self.randomButtonContainer)
		
		#avearage
		self.averageButtonContainer = QtWidgets.QVBoxLayout()
		self.averageButtonContainer.setObjectName("averageButtonContainer")
		self.averageButton = QtWidgets.QPushButton(self.rootContainer)
		self.averageButton.setMinimumSize(QtCore.QSize(0, 20))
		self.averageButton.setObjectName("averageButton")
		self.averageButtonContainer.addWidget(self.averageButton)
		self.buttonsContainer.addLayout(self.averageButtonContainer)
		self.gridLayout_2.addLayout(self.buttonsContainer, 17, 0, 1, 1)
		

		"/////////// SROLLAREA & SLIDERS ///////////"
		
		self.scrollAreaContainer = QtWidgets.QGridLayout()
		self.scrollAreaContainer.setObjectName("scrollAreaContainer")
		self.scrollArea = QtWidgets.QScrollArea(self.rootContainer)
		
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
		
		self.scrollArea.setSizePolicy(sizePolicy)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		
		self.scrollWidgetContents = QtWidgets.QWidget()
		self.scrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 156, 720))
		self.scrollWidgetContents.setMinimumSize(QtCore.QSize(0, 720))
		self.scrollWidgetContents.setObjectName("scrollWidgetContents")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollWidgetContents)
		self.verticalLayout_3.setObjectName("verticalLayout_3")

		#keys and range of slider

		bucket = []
		for pair in SLIDER_NUM.items():
			bucket.append(pair)

		for i in range(len(bucket)):
			self.sliderContainer = QtWidgets.QWidget(self.scrollWidgetContents)
			self.sliderContainer.setMinimumSize(QtCore.QSize(0, 40)) 
			self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sliderContainer)
			self.sliderLabel = QtWidgets.QLabel(self.sliderContainer)
			self.sliderLabel.setText(bucket[i][0])
			self.verticalLayout_5.addWidget(self.sliderLabel)
			self.horizontalSlider = QtWidgets.QSlider(self.sliderContainer)
			self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
			
			#slidervalues
			self.horizontalSlider.setMinimum(0)
			self.horizontalSlider.setMaximum(bucket[i][1])
			self.horizontalSlider.setValue(random.randrange(1,bucket[i][1]))
			self.horizontalSlider.setTickPosition(self.horizontalSlider.TicksBelow)
			self.horizontalSlider.setTickInterval(bucket[i][1]//5)
			
			self.verticalLayout_5.addWidget(self.horizontalSlider)
			self.seperator = QtWidgets.QFrame(self.sliderContainer)
			self.seperator.setFrameShape(QtWidgets.QFrame.HLine)
			self.seperator.setFrameShadow(QtWidgets.QFrame.Sunken)
			self.verticalLayout_5.addWidget(self.seperator)
			self.verticalLayout_3.addWidget(self.sliderContainer)

		self.scrollArea.setWidget(self.scrollWidgetContents)
		self.scrollAreaContainer.addWidget(self.scrollArea, 0, 1, 1, 1)
		self.gridLayout_2.addLayout(self.scrollAreaContainer, 1, 0, 16, 1)

		"/////////// COMBOBOX ///////////"
		self.comboBoxContainer = QtWidgets.QVBoxLayout()
		self.comboBoxContainer.setObjectName("comboBoxContainer")
		self.comboBox = QtWidgets.QComboBox(self.rootContainer)
		self.comboBox.setMinimumSize(QtCore.QSize(0, 20))
		self.comboBox.setObjectName("comboBox")
		self.comboBox.addItem("Faces")
		#just add string to add cars/abstracts/fishes etc. if you want
		self.comboBox.addItem("Placeholder") 
		self.comboBox.addItem("Placeholder")
		self.comboBoxContainer.addWidget(self.comboBox)
		self.gridLayout_2.addLayout(self.comboBoxContainer, 0, 0, 1, 1)


		"/////////// SPACING ETC. ///////////"

		self.hr1 = QtWidgets.QHBoxLayout()
		self.hr1.setObjectName("hr1")
		self.widget = QtWidgets.QWidget(self.rootContainer)
		self.widget.setObjectName("widget")
		self.hr1.addWidget(self.widget)
		self.gridLayout_2.addLayout(self.hr1, 1, 6, 16, 1)

		self.hr0 = QtWidgets.QHBoxLayout()
		self.hr0.setObjectName("hr0")
		self.widget0 = QtWidgets.QWidget(self.rootContainer)
		self.widget0.setObjectName("widget0")
		self.hr0.addWidget(self.widget0)
		self.gridLayout_2.addLayout(self.hr0, 1, 1, 16, 1)


		"/////////// IMAGEBOX ///////////"

		self.imageBoxContainer = QtWidgets.QWidget(self.rootContainer)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.imageBoxContainer.sizePolicy().hasHeightForWidth())
		self.imageBoxContainer.setSizePolicy(sizePolicy)
		self.imageBoxContainer.setMinimumSize(QtCore.QSize(412, 412))
		self.imageBoxContainer.setObjectName("imageBoxContainer")
		self.gridLayout = QtWidgets.QGridLayout(self.imageBoxContainer)
		self.gridLayout.setObjectName("gridLayout")
		self.imageBox = QtWidgets.QLabel(self.imageBoxContainer)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.imageBox.sizePolicy().hasHeightForWidth())
		
		self.imageBox.setSizePolicy(sizePolicy)
		self.imageBox.setMinimumSize(QtCore.QSize(412, 412))
		self.imageBox.setSizeIncrement(QtCore.QSize(1, 1))
		self.imageBox.setPixmap(QtGui.QPixmap("icon.png"))
		self.imageBox.setScaledContents(True)
		self.imageBox.setObjectName("imageBox")
		self.gridLayout.addWidget(self.imageBox, 0, 0, 1, 1)
		self.gridLayout_2.addWidget(self.imageBoxContainer, 0, 5, 18, 1)

		Window.setCentralWidget(self.rootContainer)

		self.retranslateUi(Window)
		QtCore.QMetaObject.connectSlotsByName(Window)

	def retranslateUi(self, Window):
		_translate = QtCore.QCoreApplication.translate
		Window.setWindowTitle(_translate("Window", "MainWindow"))
		self.randomButton.setText(_translate("Window", "Random"))
		self.averageButton.setText(_translate("Window", "Average"))

	def randomize(self):
		import os, sys
		os.execv(sys.executable, ['python3'] + sys.argv)


if __name__ == "__main__":
	import sys  
	app = QtWidgets.QApplication(sys.argv)
	Window = QtWidgets.QMainWindow()
	ui = Ui_Window()
	ui.setupUi(Window)
	Window.show()
	sys.exit(app.exec_())
