# Libraries that we will be using to work with pictures mainly to just read in images and work with their pixels.
# import cv2
from PIL import Image

#
# img = cv2.imread("tests/testPhotos/beach.jpeg")
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Start of program. Describe what the program will do and then ask for a path for the image file
# they want to alter.
print("Image Alterer Version 0.0")
imageFile = raw_input("Please specify the path to the image  you wish to alter: ")

print("Here are the list of features available")
menu = True
while menu == True:
    print("1 : Flip")
    print("2 : Rotate")
    print("3 : Mirror")
    print("0 : Exit Program")
    choice = raw_input("Please enter in the number of the feature : ")

    if choice == "1":
        print("1")
    elif choice == "2":
        print("2")
    elif choice == "3":
        print("3")
    elif choice == "0":
        menu = False

# im = Image.open('tests/testPhotos/beach.jpeg')
im = Image.open(imageFile)
size = im.size
print(size);
pixels = im.load()
print(pixels[30,30])

'''
Using size we can loop through all the pixels and manipulate them however we wish
'''
for x in range(350):
    pixels[x, 30] = (0,0,0)


im.save("test.jpg")
'''
Have to install cv2 using pip install opencv-python
and Pillow using pip install Pillow
'''
