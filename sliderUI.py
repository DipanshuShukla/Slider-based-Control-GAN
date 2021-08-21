from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import random

class Ui_UI(object):

	def __init__(self, z_dimention,ranges):
		self.totalSliders = z_dimention
		self.ranges = ranges
		self.sliders =None
		self.update_image = True

	def _sliderBox_creator(self,id,range_):

		self.sliderBox = QtWidgets.QWidget(self.sliderCont)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sliderBox.sizePolicy().hasHeightForWidth())
		self.sliderBox.setSizePolicy(sizePolicy)
		self.sliderBox.setMinimumSize(QtCore.QSize(0, 60))
		self.sliderBox.setObjectName("sliderBox")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sliderBox)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.label = QtWidgets.QLabel(self.sliderBox)
		self.label.setObjectName("label")
		self.label.setText(f"PCA #{id+1}")
		self.verticalLayout_4.addWidget(self.label)
		self.horizontalSlider = QtWidgets.QSlider(self.sliderBox)
		self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider.setObjectName("horizontalSlider")
		self.verticalLayout_4.addWidget(self.horizontalSlider)
		self.verticalLayout_5.addWidget(self.sliderBox)
		self.verticalLayout_3.addWidget(self.sliderCont)
		
		#print(range_)
		self.horizontalSlider.setMinimum(range_[0])
		self.horizontalSlider.setMaximum(range_[1])
		self.horizontalSlider.setSliderPosition(sum(range_)//2)
		
		

		return self.horizontalSlider

	def setupUi(self, UI):
		UI.setObjectName("UI")
		UI.setWindowModality(QtCore.Qt.NonModal)
		UI.resize(1109, 743)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(UI.sizePolicy().hasHeightForWidth())
		UI.setSizePolicy(sizePolicy)
		UI.setMinimumSize(QtCore.QSize(1109, 743))
		UI.setMouseTracking(False)
		UI.setTabletTracking(False)
		UI.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		UI.setWindowIcon(icon)
		UI.setLayoutDirection(QtCore.Qt.LeftToRight)
		UI.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.centralwidget = QtWidgets.QWidget(UI)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout_4.setObjectName("gridLayout_4")


		self.scrollAreaCont = QtWidgets.QVBoxLayout()
		self.scrollAreaCont.setObjectName("scrollAreaCont")
		self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
		self.scrollArea.setSizePolicy(sizePolicy)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 358, 551))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.sliderCont = QtWidgets.QWidget(self.scrollAreaWidgetContents)
		self.sliderCont.setObjectName("sliderCont")
		self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sliderCont)
		self.verticalLayout_5.setObjectName("verticalLayout_5")


		#slider
		if __name__ == "__main__":
			self.create_sliders()


		
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.scrollAreaCont.addWidget(self.scrollArea)
		self.gridLayout_4.addLayout(self.scrollAreaCont, 2, 0, 12, 1)
		


		self.comboCont = QtWidgets.QHBoxLayout()
		self.comboCont.setObjectName("comboCont")
		self.comboBox = QtWidgets.QComboBox(self.centralwidget)
		self.comboBox.setObjectName("comboBox")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.comboCont.addWidget(self.comboBox)
		self.gridLayout_4.addLayout(self.comboCont, 0, 0, 1, 1)


		self.btnCont = QtWidgets.QHBoxLayout()
		self.btnCont.setObjectName("btnCont")
		self.rndCont = QtWidgets.QHBoxLayout()
		self.rndCont.setObjectName("rndCont")
		self.rndBtn = QtWidgets.QPushButton(self.centralwidget)
		self.rndBtn.setObjectName("rndBtn")
		
		self.rndCont.addWidget(self.rndBtn)
		self.btnCont.addLayout(self.rndCont)
		self.avgCont = QtWidgets.QHBoxLayout()
		self.avgCont.setObjectName("avgCont")
		self.avgBtn = QtWidgets.QPushButton(self.centralwidget)
		self.avgBtn.setObjectName("avgBtn")
		self.avgCont.addWidget(self.avgBtn)
		self.btnCont.addLayout(self.avgCont)
		self.gridLayout_4.addLayout(self.btnCont, 14, 0, 1, 1)

		self.rndBtn.clicked.connect(self.randomize)
		self.avgBtn.clicked.connect(self.set_average)


		#layer slider
		self.layerCont = QtWidgets.QVBoxLayout()
		self.layerCont.setObjectName("layerCont")
		self.layerBox = QtWidgets.QFrame(self.centralwidget)
		self.layerBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.layerBox.setFrameShadow(QtWidgets.QFrame.Raised)
		self.layerBox.setObjectName("layerBox")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.layerBox)
		self.verticalLayout.setObjectName("verticalLayout")
		self.layerLabel = QtWidgets.QLabel(self.layerBox)
		self.layerLabel.setObjectName("layerLabel")
		self.verticalLayout.addWidget(self.layerLabel)
		self.layerSlider = QtWidgets.QSlider(self.layerBox)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.layerSlider.sizePolicy().hasHeightForWidth())
		self.layerSlider.setSizePolicy(sizePolicy)
		self.layerSlider.setOrientation(QtCore.Qt.Horizontal)
		self.layerSlider.setObjectName("layerSlider")
		self.verticalLayout.addWidget(self.layerSlider)
		self.layerCont.addWidget(self.layerBox)
		self.gridLayout_4.addLayout(self.layerCont, 1, 0, 1, 1)



		
		self.imgBoxCont = QtWidgets.QWidget(self.centralwidget)
		self.imgBoxCont.setObjectName("imgBoxCont")
		self.imgCont = QtWidgets.QGridLayout(self.imgBoxCont)
		self.imgCont.setObjectName("imgCont")
		self.imgBox = QtWidgets.QLabel(self.imgBoxCont)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.imgBox.sizePolicy().hasHeightForWidth())
		self.imgBox.setSizePolicy(sizePolicy)
		self.imgBox.setMaximumSize(QtCore.QSize(720, 720))
		self.imgBox.setText("")
		self.imgBox.setPixmap(QtGui.QPixmap("avatar.jpeg"))
		self.imgBox.setScaledContents(True)
		self.imgBox.setObjectName("imgBox")
		self.imgCont.addWidget(self.imgBox, 0, 0, 1, 1)
		self.gridLayout_4.addWidget(self.imgBoxCont, 0, 1, 15, 2)
		UI.setCentralWidget(self.centralwidget)

		self.retranslateUi(UI)
		QtCore.QMetaObject.connectSlotsByName(UI)

	def retranslateUi(self, UI):
		_translate = QtCore.QCoreApplication.translate
		UI.setWindowTitle(_translate("UI", "MainWindow"))
		#self.label.setText(_translate("UI", "TextLabel"))
		self.comboBox.setItemText(0, _translate("UI", "Faces"))
		self.comboBox.setItemText(1, _translate("UI", "Cars"))
		self.rndBtn.setText(_translate("UI", "Randomize"))
		self.avgBtn.setText(_translate("UI", "Average"))
		self.layerLabel.setText(_translate("UI", "Layers"))

	def randomize(self):
		self.update_image = False
		
		for i in range(self.totalSliders-1):
		#for i in range(10):
			range_ = self.ranges[i]
			self.sliders[i].setSliderPosition(random.randint(int(range_[0]),int(range_[1])+1))
		self.update_image = True
		range_ = self.ranges[self.totalSliders-1]
		self.sliders[self.totalSliders-1].setSliderPosition(random.randint(int(range_[0]),int(range_[1])+1))

	def set_average(self):
		self.update_image = False

		for i in range(self.totalSliders-1):
			range_ = self.ranges[i]
			self.sliders[i].setSliderPosition(sum(range_)//2)
		self.update_image = True
		range_ = self.ranges[self.totalSliders-1]
		self.sliders[self.totalSliders-1].setSliderPosition(sum(range_)//2)

	def get_z(self):
		#return np.array([slider.value() for slider in self.sliders])
		return [slider.value() for slider in self.sliders]

	def set_img(self,img):
		qImg = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.shape[1]*3, QtGui.QImage.Format_RGB888)
		self.imgBox.setPixmap(QtGui.QPixmap(qImg))

	def create_sliders(self):
		self.sliders = []
		for i in range(self.totalSliders):
			self.sliders.append(self._sliderBox_creator(i,self.ranges[i]))



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	UI = QtWidgets.QMainWindow()
	totalSliders = 512
	ui = Ui_UI(totalSliders, range_:=[[ini:=random.randint(0, 10), random.randint(ini+20, 50)] for i in range(totalSliders)])
	#print(range_)
	ui.setupUi(UI)
	UI.show()

	import cv2
	ui.set_img(cv2.imread("avatar.jpeg"))

	sys.exit(app.exec_())