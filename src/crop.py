## this function is responsible for croping an image with given dimensions
from PIL import Image

def crop(im,xStart,xEnd,yStart,yEnd):
    ## get the dimensions and pixels from the original image
    size = im.size
    pixels = im.load()

    ## if invalid crop dimensions given by user then return error message
    ## same image is returned back with no change if invalid dimensions.
    if xStart > xEnd or yStart > yEnd:
        print("Invalid crop dimensions given")
        return im

    if xEnd+1 > size[0] or yEnd+1 > size[1]:
        print("Invalid crop dimensions given")
        return im

    crop_width = xEnd - xStart + 1
    crop_height = yEnd - yStart + 1

    ## intialize the new image with new dimensions based on crop inputs
    newImg = Image.new('RGB', (crop_width,crop_height), 0)
    newPixels = newImg.load()

    mir_width = size[0] - 1
    mir_height = 0

    relativex = xStart
    relativey = yStart
    cropx = 0
    cropy = 0




    ## iterate through each pixel and place the pixel in new cropped dimensions
    for y in range(size[1]):
        for x in range(size[0]):
            if x == relativex and y == relativey:
                newPixels[cropx,cropy] = pixels[x,y]
                cropx = cropx + 1
                if cropx == crop_width:
                    cropx = 0
                    cropy = cropy + 1
                relativex = relativex + 1
                if relativex > xEnd:
                    relativex = xStart
                    relativey = relativey + 1
        if cropy == crop_height:
            break


    return newImg
