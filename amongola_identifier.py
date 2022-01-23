#Load and show an image with Pillow
from PIL import Image
import random


#Load the image
# IMPORTANT NOTE: You must run this program while inside the folder also containing the following image.
# Otherwise, you will have to specify an exact file path, which of course differs between machines.
image = Image.open('amongus_trashcan.jpg')

#Convert it to gray-scale
image_grayscale = image.convert('L')

#Outline to be overlayed
amongus_outline = Image.open('amongus_outline.png')

#rotate randomly
amongus_outline = amongus_outline.rotate(random.randint(0,360))

#Pasting outline on top of image
#starting at coordinates (0, 0)
image.paste(amongus_outline, (0,0), mask = amongus_outline)
  
# Displaying the image
image.show()
