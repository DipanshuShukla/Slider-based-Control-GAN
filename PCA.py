import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt


class PCA:
	def __init__(self):
		self.pca = PCA(n_components=1)
		self.data = None
		