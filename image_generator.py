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
		self.pickle_path = "./models/pretrained/stylegan2-ffhq-config-f.pkl"
		self.pickle_path = "./models/pretrained/stylegan2-car-config-f.pkl"

		self._G, self._D, self.Gs = None, None, None

		self.import_pickle()
		self.z = np.random.RandomState(0).randn(*self.Gs.input_shape[1:])

		self.w = self.Gs.components.mapping.run(np.stack([self.z]), None)

		self.Gs_syn_kwargs = dnnlib.EasyDict()
		self.Gs_syn_kwargs.output_transform = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
		self.Gs_syn_kwargs.randomize_noise = False
		self.Gs_syn_kwargs.minibatch_size = 4

	def import_pickle(self):

		print("Pickle Loading...")

		with open(self.pickle_path, 'rb') as f:
			self._G, self._D, self.Gs = pickle.load(f)

		self.set_W_avg()


		print("Pickle Loaded.")

	def set_Z(self,z):
		self.z = z

	def set_W(self):
		self.w = self.Gs.components.mapping.run(np.stack([self.z]), None)

	def set_W_avg(self):
		self.w = self.Gs.get_var('dlatent_avg')

	def generate_image(self):
		return self.Gs.components.synthesis.run(self.w, **self.Gs_syn_kwargs)[0]



if __name__ == "__main__":
	Igen = ImageGenGAN()

	Igen.pickle_path = "./models/pretrained/stylegan2-car-config-f.pkl"

	import matplotlib.pyplot as plt
	for seed in range(1357,1377):
		Igen.set_Z(np.random.RandomState(seed).randn(*Igen.Gs.input_shape[1:]))
		Igen.set_W()
		plt.imshow(Igen.generate_image())
		plt.show()