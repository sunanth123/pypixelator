## This function is responsible for rotating an image by the degrees specified
## by the user (either 90, 180, or 270 degree rotation). By using nested for
## loops can iterate through each individual pixel of original passed in image
## and add the appropriate pixel to the newly rotated image.
from PIL import Image

def rotate(im,rotate):

    ## get the dimensions and pixels from the passed in original image
    size = im.size
    pixels = im.load()
    newImg = None

    ## if selected to rotate image 180 degrees
    if rotate == 180:
        ## new image will have the same dimensions as the original
        newImg = Image.new('RGB', size, 0)
        newPixels = newImg.load()
        rot_width = size[0] - 1
        rot_height = size[1] - 1

        ## iterate through the pixels of the original image and add to the
        ## new image from bottom to top.
        for y in range(size[1]):
            for x in range(size[0]):
                newPixels[x,y] = pixels[rot_width,rot_height]
                rot_width = rot_width - 1
            rot_width = size[0] - 1
            rot_height = rot_height - 1

    ## if selected to rotate image 90 degrees
    elif rotate == 90:
        ## dimensions of size will be inverted from the original
        newsize = (size[1],size[0])
        newImg = Image.new('RGB', newsize, 0)
        newPixels = newImg.load()
        rot_width = newsize[0] - 1
        rot_height = 0

        ## iterate the original image and add respective pixel to the newly
        ## made image with inverted dimensions.
        for y in range(size[1]):
            for x in range(size[0]):
                newPixels[rot_width,rot_height] = pixels[x,y]
                rot_height = rot_height + 1
            rot_height = 0
            rot_width = rot_width - 1

    ## if selected to rotate image 270 degrees
    elif rotate == 270:
        ## dimensions of size will be inverted from the original
        newsize = (size[1],size[0])
        newImg = Image.new('RGB', newsize, 0)
        newPixels = newImg.load()
        rot_width = 0
        rot_height = newsize[1] - 1

        ## iterate the original image and add respective pixel to the newly
        ## made image with inverted dimensions.
        for y in range(size[1]):
            for x in range(size[0]):
                newPixels[rot_width,rot_height] = pixels[x,y]
                rot_height = rot_height - 1
            rot_height = newsize[1] - 1
            rot_width = rot_width + 1

    ## if invalid degree rotation is provided then print error message and
    ## return original image
    else:
        print("Invalid degree rotation")
        return im

    ## return the final image after rotation is made
    return newImg
