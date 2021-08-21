from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import random
import image_generator, testUI
from PCA import PCA
from copy import deepcopy

class GAN_UI(testUI.Ui_UI):
	def load_GAN(self):

		self.Gan_ = image_generator.ImageGenGAN()
		self.pca = PCA(self.Gan_)

		self.totalSliders = self.pca.no_of_PC
		print(self.totalSliders)
		self.ranges = [[0,self.pca.per_var[1]*100] for i in range(self.totalSliders)]

		self.create_sliders()
		self.connect_sliders()
		self.update_UI_image()

	def connect_sliders(self):
		for i in range(self.totalSliders):
			self.sliders[i].valueChanged.connect(self.update_UI_image)

	def update_UI_image(self):
		if self.update_image:
			#print(f"inverse PCA = {len(self.pca.reverse_PCA(self.get_z()))}")
			self.Gan_.set_Z((self.Gan_.z + self.pca.reverse_PCA(self.get_z())) - self.Gan_.z)
			#self.Gan_.set_Z(np.array[np.array(self.pca.reverse_PCA(self.get_z())) * 18])
			print(self.Gan_.get_W(1).shape)
			#self.Gan_.set_Z(np.stack([[deepcopy(self.pca.reverse_PCA(self.get_z())) for i in range(18)]], None))
			print(self.Gan_.z.shape)

			#return
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
	ui.load_GAN()
	UI.show()
	#import cv2
	#ui.set_img(cv2.imread("avatar.jpeg"))

	sys.exit(app.exec_())


	