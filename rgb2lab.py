from skimage import io, color
from matplotlib import pyplot as plt
rgb = io.imread('196.jpg')
lab = color.rgb2lab(rgb)

print(lab)
# print lab
# print (io.imshow(lab))
# plt.show()