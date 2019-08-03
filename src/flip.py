# Flips the image along the x axis. Uses loops to iterate through all the pixels placing them
# in their flipped posistions
from PIL import Image

def flip(im):
    #Create a new image first and then copy over the pixels in the flipped placements
    size = im.size
    pixel = im.load()
    newImg = Image.new('RGB', size, 0)
    newPixels = newImg.load()

    #Variables to hold the height and width of the flip happening
    flip_width = size[0] - 1
    flip_height = 0
    for x in range(size[0]):
        for y in range(size[1]):
            newPixels[x,y] = pixels[flip_width,y]
        flip_width = flip_width - 1

    return newImg
    # print(pixels)
