from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import random
import image_generator, testUI

class GAN_UI(testUI.Ui_UI):
	def load_GAN(self):

		self.Gan_ = image_generator.ImageGenGAN()
		self.totalSliders = self.Gan_.Gs.input_shape[-1]
		print(self.totalSliders)
		self.ranges = [[0,255] for i in range(self.totalSliders)]

		self.create_sliders()
		self.connect_sliders()

	def connect_sliders(self):
		for i in range(self.totalSliders):
			self.sliders[i].valueChanged.connect(self.update_image)

	def update_image(self):
		#print(self.get_z())
		self.Gan_.set_Z(np.random.RandomState(self.get_z()[0]).randn(self.Gan_.Gs.input_shape[-1]))
		self.Gan_.set_W()

		self.set_img(self.Gan_.generate_image())



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	UI = QtWidgets.QMainWindow()
	totalSliders = 20
	ui = GAN_UI(totalSliders, range_:=[[ini:=random.randint(0, 10), random.randint(ini+20, 50)] for i in range(totalSliders)])
	#print(range_)
	
	ui.setupUi(UI)
	
	UI.show()
	
	ui.load_GAN()
	#import cv2
	#ui.set_img(cv2.imread("avatar.jpeg"))

	sys.exit(app.exec_())


	