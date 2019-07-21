# Libraries that we will be using to work with pictures mainly to just read in images and work with their pixels.
# import cv2
from PIL import Image
import numpy as np

'''Import functions from other files'''
from src.flip import flip
from src.rotate import rotate
from src.mirror import mirror
#
# img = cv2.imread("tests/testPhotos/beach.jpeg")
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Start of program. Describe what the program will do and then ask for a path for the image file
# they want to alter.
print("Image Alterer Version 0.0")
imageFile = raw_input("Please specify the path to the image  you wish to alter: ")

# im = Image.open('tests/testPhotos/beach.jpeg')
im = Image.open(imageFile)
size = im.size
print(size);
pixels = im.load()


print("Here are the list of features available")
menu = True
while menu == True:
    print("1 : Flip")
    print("2 : Rotate")
    print("3 : Mirror")
    print("0 : Exit Program")
    choice = raw_input("Please enter in the number of the feature : ")

    if choice == "1":
        im = flip(pixels, size)
    elif choice == "2":
        rotate()
    elif choice == "3":
        mirror()
    elif choice == "0":
        menu = False

'''
Using size we can loop through all the pixels and manipulate them however we wish
'''
# for x in range(700):
#     pixels[x, 30] = (0,0,0)
# pixel_array = np.array(pixels, dtype=np.uint8)
# final_image = Image.fromarray(pixel_array)
# final_image.save("test.jpg")
im.save("test.jpg")
'''
Have to install cv2 using pip install opencv-python
and Pillow using pip install Pillow
'''
