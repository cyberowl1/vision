from PIL import Image
import os
import matplotlib.pyplot as plt
from PIL import ImageOps
import cv2



my_image = "lenna.png"

image = os.path.join(os.getcwd(), my_image)

# i_mage = Image.open(image)
# i_mage.show()

# plot

# plt.figure(figsize=(12,12))
# plt.imshow(i_mage)
# plt.show()

# print(i_mage.size)
# print(i_mage.mode)

# im = i_mage.load()
# x = 0
# y = 0

# print(im[x,y])

# image_grey = ImageOps.grayscale(i_mage)

# image_grey.save("glemaa.png")


# baboon = Image.open("baboon.png")
# split in all 3 channel
# red, green , blue = baboon.split()
# #

# blue.save("bblue.png")
# green.save("green.png")

# im = cv2.imread(my_image)
# print(type(im))
# print(im.shape)


# opencv2

# baboon_blue=cv2.imread('baboon.png')
# baboon_blue=cv2.cvtColor(baboon_blue, cv2.COLOR_BGR2RGB)
# baboon_blue[:,:,2] = 0

# image show using matplotlib
# plt.figure(figsize=(10,10))
# plt.imshow(baboon_blue)
# plt.show()