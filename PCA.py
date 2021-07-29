import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA as skPCA
from sklearn import preprocessing
import matplotlib.pyplot as plt
import random

NO_OF_SEEDS = 20000
NO_OF_PC = 20

class PCA:
	def __init__(self,GAN_):
		
		global NO_OF_SEEDS, NO_OF_PC

		self.no_of_PC = NO_OF_PC

		self.pca = skPCA(n_components = self.no_of_PC)
		self.data = None
		self.GAN_ = GAN_

		self.W_shape = self.GAN_.Gs.input_shape[-1]

		self.seeds = [random.randint(0,9999) for i in range(NO_OF_SEEDS)]

		self.generate_samples()

		self.scaled_data = preprocessing.scale(self.data)
		print("Fitting PCA model...")
		self.pca_data = self.pca.fit_transform(self.scaled_data)

		self.per_var = np.round(self.pca.explained_variance_ratio_* 100, decimals=1)

		print("Done.")

	def generate_samples(self):
		self.data = pd.DataFrame([self.GAN_.get_W(seed)[0][0] for seed in self.seeds], index = self.seeds)
		print(self.data)

	def reverse_PCA(self,pc):
		return self.pca.inverse_transform(pc)

		

if __name__ == "__main__":

	from image_generator import ImageGenGAN
	GAN_ = ImageGenGAN()

	pca = PCA(GAN_)

	print("plotting...")
	labels = ['PC' + str(x) for x in range(1, len(pca.per_var)+1)]
	plt.bar(x=range(1,len(pca.per_var)+1), height=pca.per_var, tick_label=labels)
	plt.ylabel('Percentage of Explained Variance')
	plt.xlabel('Principal Component')
	plt.title('Scree Plot')
	plt.show()

	print("done.")



