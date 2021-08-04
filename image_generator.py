import sys
sys.path.insert(0,"./models")

import dnnlib.tflib as tflib
import dnnlib

import pickle
import os
import numpy as np
import matplotlib.pyplot as plt

# StyleGAN only works on tensorflow v1.x
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# Silence deprecation warnings from TensorFlow 1.13 onwards
import logging
logging.getLogger('tensorflow').setLevel(logging.ERROR)


class ImageGenGAN:
	def __init__(self):

		tflib.init_tf()
		self.pickle_path = "./models/pretrained/stylegan2-ffhq-config-f.pkl" # 9fps
		#self.pickle_path = "./models/pretrained/stylegan2-car-config-f.pkl" # 14fps

		self._G, self._D, self.Gs = None, None, None

		self.import_pickle()
		self.z = np.random.RandomState(0).randn(*self.Gs.input_shape[1:])

		self.w = self.Gs.components.mapping.run(np.stack([self.z]), None)

		self.Gs_syn_kwargs = dnnlib.EasyDict()
		self.Gs_syn_kwargs.output_transform = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
		self.Gs_syn_kwargs.randomize_noise = False
		self.Gs_syn_kwargs.minibatch_size = 4

		self.generate_image() # to initialise and test

	def import_pickle(self):

		print("Pickle Loading...")

		with open(self.pickle_path, 'rb') as f:
			self._G, self._D, self.Gs = pickle.load(f)


		print("Pickle Loaded.")

	def set_Z(self,z):
		self.z = z

	def set_W(self):
		self.w = self.Gs.components.mapping.run(np.stack([self.z]), None)

	def get_W(self,seed):
		return self.Gs.components.mapping.run(np.stack([np.random.RandomState(seed).randn(*self.Gs.input_shape[1:])]), None)

	def generate_image(self):
		return self.Gs.components.synthesis.run(self.w, **self.Gs_syn_kwargs)[0]



if __name__ == "__main__":
	Igen = ImageGenGAN()

	Igen.pickle_path = "./models/pretrained/stylegan2-car-config-f.pkl"

	import cv2, time

	#Igen.generate_image()

	print("Generating 60 images...")

	start = time.time()

	seed = 1

	while True:
	#for seed in range(1340,1400):
		#seed = 1
		Igen.set_Z(np.random.RandomState(seed).randn(*Igen.Gs.input_shape[1:]))
		Igen.set_W()


		cv2.imshow("images",cv2.cvtColor(Igen.generate_image(), cv2.COLOR_BGR2RGB))
		cv2.waitKey(1)

		if time.time() - start >= 0.5:
			seed +=1
			start = time.time()


	time_taken = time.time() - start

	print(f"Completed in {time_taken} seconds.")
	print(f"resulted in approx. {60//time_taken} fps.")