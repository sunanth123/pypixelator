## this function is responsible for pixelating an image based on the
## coordinates given by the user.
from PIL import Image

def pixel(im,factor,xStart,xEnd,yStart,yEnd):
    ## get the dimensions and pixels from the original image and initialize
    ## a new image with the same size.
    size = im.size
    pixels = im.load()
    newImg = Image.new('RGB', size, 0)
    newPixels = newImg.load()

    ## check if dimensions are valid, if not return same image back
    if xStart > xEnd or yStart > yEnd:
        print("Invalid pixelate dimensions given")
        return im

    if xEnd > size[0] or yEnd > size[1]:
        print("Invalid pixelate dimensions given")
        return im

    if factor < 1 or factor > 5:
        print("Invalid pixelation value, choose from 1-5")
        return im

    for y in range(size[1]):
        for x in range(size[0]):
            newPixels[x,y] = pixels[x,y]

    pixelate = factor * 2
    # xStart = 0
    # yStart = 0
    # xEnd = size[0]
    # yEnd = size[1]

    ## iterate through original image and with each pixel representing a
    ## block that new pixel will be copied over to the final image.
    for x in range(xStart,xEnd):
        for y in range(yStart,yEnd):
            if x % pixelate == 0 and y % pixelate == 0:
                for nx in range(x,x+pixelate+1):
                    for ny in range(y,y+pixelate+1):
                        if nx < xEnd and ny < yEnd:
                            newPixels[nx,ny] = pixels[x,y]

    return newImg
