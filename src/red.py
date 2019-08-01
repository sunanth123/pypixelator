## this function is responsible for converting an image into red scale.
from PIL import Image

def red(im):
    ## get the dimensions and pixels from the original image and initialize
    ## a new image with the same size.
    size = im.size
    pixels = im.load()
    newImg = Image.new('RGB', size, 0)
    newPixels = newImg.load()

    ## Iterate through each pixel of the original image and then place the pixel
    ## in the same position for the new image. The new pixel is an average of
    ## the red,green,blue pixel values of the original image. The resulting
    ## average is then used as the new RGB values for the new pixel, while
    ## keeping the red value at its max value fo 255.
    for y in range(size[1]):
        for x in range(size[0]):
            single_pixel=im.getpixel((x,y))
            gray = (single_pixel[0] + single_pixel[1] + single_pixel[2])/3
            newImg.putpixel((x,y),(255,gray,gray))

    return newImg
