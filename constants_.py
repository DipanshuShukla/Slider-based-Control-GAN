from PIL import Image
from numpy import asarray

import matplotlib.pyplot as plt

# load the image
IMAGE = Image.open('avatar.jpeg')


NO_SLIDERS = 10
SLIDERS_RANGES = []


def get_img(l):
	
	return asarray(IMAGE)


if __name__ == "__main__":
	plt.imshow(get_img(1))
	plt.show()