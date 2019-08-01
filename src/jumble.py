## this function will jumble up the pixels of the passed in image
from PIL import Image
from random import shuffle

def jumble(im):
    ## get the dimensions and pixels from the original image and initialize
    ## a new image with the same size.
    size = im.size
    pixels = im.load()
    newImg = Image.new('RGB', size, 0)
    newPixels = newImg.load()
    rand_coord = []
    count = 0

    ## get all the coordinants of original image and shuffle the coordinants
    for x in range(size[0]):
        for y in range(size[1]):
            rand_coord.append([x,y])

    shuffle(rand_coord)

    ## Iterate through each pixel of the original image and then place the pixel
    ## in a random coordinant of the new image.
    for y in range(size[1]):
        for x in range(size[0]):
            newPixels[rand_coord[count][0],rand_coord[count][1]] = pixels[x,y]
            count = count + 1

    return newImg
