## this function is responsible for doubling the dimensions of the image given
from PIL import Image

def enlarge(im):
    ## get the dimensions and pixels from the original image and initialize
    ## a new image with the double the dimensions.
    size = im.size
    pixels = im.load()
    newImg = Image.new('RGB', (size[0]*2,size[1]*2), 0)
    newPixels = newImg.load()

    width = 0
    height = 0
    ## Iterate through each pixel of the original image and then place the pixel
    ## in a block that is double the dimensions for the new image.
    for y in range(size[1]):
        for x in range(size[0]):
            newPixels[width,height] = pixels[x,y]
            newPixels[width+1,height] = pixels[x,y]
            newPixels[width,height+1] = pixels[x,y]
            newPixels[width+1,height+1] = pixels[x,y]
            width = width + 2
        width = 0
        height = height + 2

    print(size)
    print(newImg.size)
    return newImg
