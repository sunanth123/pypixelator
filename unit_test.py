## This file contains the unit tests for each of the image functions.
## compares newly modified image to what its expected to be.
from PIL import Image
import numpy as np
import unittest
import os
import sys
from PIL import ImageChops
'''Import functions from other files'''
from src.flip import flip
from src.rotate import rotate
from src.mirror import mirror
from src.gray import gray
from src.enlarge import enlarge
from src.crop import crop
from src.red import red
from src.blue import blue
from src.green import green
from src.jumble import jumble


fileDir = os.path.dirname(os.path.abspath(__file__))

class Test(unittest.TestCase):
    def test_bluescale(self):
        print("\nStarting blue scale test")
        im = Image.open(fileDir + "/tests/testPhotos/beach.jpeg")
        testim = Image.open(fileDir + "/tests/testPhotos/test_blue.jpg")
        im = blue(im)
        im.save("test.jpg")
        im = Image.open("test.jpg")
        test = ImageChops.difference(im,testim).getbbox()
        self.assertEqual(test,None)

    def test_crop(self):
        print("\nStarting crop test")
        im = Image.open(fileDir + "/tests/testPhotos/beach.jpeg")
        testim = Image.open(fileDir + "/tests/testPhotos/test_crop.jpg")
        im = crop(im,0,100,0,100)
        im.save("test.jpg")
        im = Image.open("test.jpg")
        test = ImageChops.difference(im,testim).getbbox()
        self.assertEqual(test,None)

    def test_enlarge(self):
        print("\nStarting enlarge test")
        im = Image.open(fileDir + "/tests/testPhotos/beach.jpeg")
        testim = Image.open(fileDir + "/tests/testPhotos/test_enlarge.jpg")
        im = enlarge(im)
        im.save("test.jpg")
        im = Image.open("test.jpg")
        test = ImageChops.difference(im,testim).getbbox()
        self.assertEqual(test,None)

    # def test_flip(self):
    #     print("\nStarting flip test")
    #     im = Image.open(fileDir + "/tests/testPhotos/beach.jpeg")
    #     testim = Image.open(fileDir + "/tests/testPhotos/test_flip.jpg")
    #     im = flip(im)
    #     im.save("test.jpg")
    #     im = Image.open("test.jpg")
    #     test = ImageChops.difference(im,testim).getbbox()
    #     self.assertEqual(test,None)

    def test_gray(self):
        print("\nStarting gray scale test")
        im = Image.open(fileDir + "/tests/testPhotos/beach.jpeg")
        testim = Image.open(fileDir + "/tests/testPhotos/test_gray.jpg")
        im = gray(im)
        im.save("test.jpg")
        im = Image.open("test.jpg")
        test = ImageChops.difference(im,testim).getbbox()
        self.assertEqual(test,None)

    def test_greencale(self):
        print("\nStarting green scale test")
        im = Image.open(fileDir + "/tests/testPhotos/beach.jpeg")
        testim = Image.open(fileDir + "/tests/testPhotos/test_green.jpg")
        im = green(im)
        im.save("test.jpg")
        im = Image.open("test.jpg")
        test = ImageChops.difference(im,testim).getbbox()
        self.assertEqual(test,None)

    def test_mirror(self):
        print("\nStarting mirror test")
        im = Image.open(fileDir + "/tests/testPhotos/beach.jpeg")
        testim = Image.open(fileDir + "/tests/testPhotos/test_mirror.jpg")
        im = mirror(im)
        im.save("test.jpg")
        im = Image.open("test.jpg")
        test = ImageChops.difference(im,testim).getbbox()
        self.assertEqual(test,None)

    def test_redscale(self):
        print("\nStarting red scale test")
        im = Image.open(fileDir + "/tests/testPhotos/beach.jpeg")
        testim = Image.open(fileDir + "/tests/testPhotos/test_red.jpg")
        im = red(im)
        im.save("test.jpg")
        im = Image.open("test.jpg")
        test = ImageChops.difference(im,testim).getbbox()
        self.assertEqual(test,None)

    def test_rotate90(self):
        print("\nStarting rotate 90 degrees test")
        im = Image.open(fileDir + "/tests/testPhotos/beach.jpeg")
        testim = Image.open(fileDir + "/tests/testPhotos/test_rotate90.jpg")
        im = rotate(im,90)
        im.save("test.jpg")
        im = Image.open("test.jpg")
        test = ImageChops.difference(im,testim).getbbox()
        self.assertEqual(test,None)

    def test_rotate180(self):
        print("\nStarting rotate 180 degrees test")
        im = Image.open(fileDir + "/tests/testPhotos/beach.jpeg")
        testim = Image.open(fileDir + "/tests/testPhotos/test_rotate180.jpg")
        im = rotate(im,180)
        im.save("test.jpg")
        im = Image.open("test.jpg")
        test = ImageChops.difference(im,testim).getbbox()
        self.assertEqual(test,None)

    def test_rotate270(self):
        print("\nStarting rotate 270 degrees test")
        im = Image.open(fileDir + "/tests/testPhotos/beach.jpeg")
        testim = Image.open(fileDir + "/tests/testPhotos/test_rotate270.jpg")
        im = rotate(im,270)
        im.save("test.jpg")
        im = Image.open("test.jpg")
        test = ImageChops.difference(im,testim).getbbox()
        self.assertEqual(test,None)



if __name__ == '__main__':
    unittest.main()
