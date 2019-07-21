# Libraries that we will be using to work with pictures mainly to just read in images and work with their pixels.
# import cv2
from PIL import Image

#
# img = cv2.imread("tests/testPhotos/beach.jpeg")
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


im = Image.open('tests/testPhotos/beach.jpeg')
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
