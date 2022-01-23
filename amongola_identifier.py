#import cv2

#background = cv2.imread('among_us_insanity.jpg')
#overlay = cv2.imread('amongus_outline.png')

#added_image = cv2.addWeighted(background,0.4,overlay,0.1,0)

#cv2.imshow('output' added_image)

#cv2.waitKey(0)
#cv2.destroyAllWindows()


#Load and show an image with Pillow
from PIL import Image

import cv2
import numpy as np
from matplotlib import pyplot as plt
  
# reading image
image = cv2.imread('among_us_insanity.jpg')

# reading overlay
#overlay = cv2.imread('amongus_outline.png')



# converting image into grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# setting threshold of gray image
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
  
# using a findContours() function
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
cv2.imwrite('amongus_outline.png', image)
  
i = 0
  
# list for storing names of shapes
for contour in contours:
  
    # here we are ignoring first counter because 
    # findcontour function detects whole image as shape
    if i == 0:
        i = 1
        continue
  
    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
      
    # using drawContours() function
    #cv2.drawContours(image, [contour], 0, (0, 0, 255), 5)
  
    # finding center point of shape
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])

    # overlay amongola outline at the center of detected shape, if it is a circle (>6 points)
    if len(approx) > 6:
        pil_image = Image.open('among_us_insanity.jpg')
        pil_overlay = Image.open('amongus_outline.png')
        image.paste(pil_overlay, (x,y), mask = pil_overlay)

# displaying the image after drawing contours
cv2.imshow('shapes', image)
  
cv2.waitKey(0)
cv2.destroyAllWindows()



#Load the image
# IMPORTANT NOTE: You must run this program while inside the folder also containing the following image.
# Otherwise, you will have to specify an exact file path, which of course differs between machines.
#image = Image.open('amongus_trashcan.jpg')

#Convert it to gray-scale
#image_grayscale = image.convert('L')

#Outline to be overlayed
#amongus_outline = Image.open('amongus_outline.png')
  
#Pasting outline on top of image
#starting at coordinates (0, 0)
#image.paste(amongus_outline, (0,0), mask = amongus_outline)
  
# Displaying the image
#image.show()



    #Pasting outline on top of image
    #cv2.imwrite('amongus_outline.png', image)
    
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
