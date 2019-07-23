## This function will mirror an image that is provided to it by using
## nested loops to iterate through the original image pixels and placing them
## in the new image in an inverted manner
from PIL import Image

def mirror(im):
    ## get the dimensions and pixels from the original image and initialize
    ## a new image with the same size.
    size = im.size
    pixels = im.load()
    newImg = Image.new('RGB', size, 0)
    newPixels = newImg.load()

    mir_width = size[0] - 1
    mir_height = 0

    ## Iterate through each pixel of the original image and then place the pixel
    ## in the opposite dimension (around the y-axis)
    for y in range(size[1]):
        for x in range(size[0]):
            newPixels[mir_width,mir_height] = pixels[x,y]
            mir_width = mir_width - 1
        mir_width = size[0] - 1
        mir_height = mir_height + 1

    return newImg
