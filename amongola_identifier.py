#Load and show an image with Pillow
from PIL import Image

#Load the image
# IMPORTANT NOTE: You must run this program while inside the folder also containing the following image.
# Otherwise, you will have to specify an exact file path, which of course differs between machines.
image = Image.open('amongus_trashcan.jpg')

#Convert it to gray-scale
image_grayscale = image.convert('L')

#Show the image
image.show()
image_grayscale.show()
