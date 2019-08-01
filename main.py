# Libraries that we will be using to work with pictures mainly to just read in images and work with their pixels.
# import cv2
from PIL import Image, ImageTk
import numpy as np
import Tkinter as tk
from Tkinter import Label, Tk, Button, Entry

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
#
# img = cv2.imread("tests/testPhotos/beach.jpeg")
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Start of program. Describe what the program will do and then ask for a path for the image file
# they want to alter.
# print("Image Alterer Version 0.0")
# imageFile = raw_input("Please specify the path to the image  you wish to alter: ")


def loadImage(path):
    im = Image.open(path)
    size = im.size
    pixels = im.load()

# im = Image.open(imageFile)
# size = im.size
# pixels = im.load()

#Class that will hold handle the GUI interface
#An instance of this class will be created and from there the program will be started
#All alterations to the image will be handled from this class
class gui(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.winfo_toplevel().title("Image Alterer Version 0.1")
        self.winfo_toplevel().geometry("800x800")
        Label(self, text='Image Alterer',font="Times 20 bold").grid(row=0, rowspan=2)
        Label(self, text='Enter in path to image below', font="Times 12 bold").grid(row=2, column=0, sticky='WS')
        self.entry = tk.Entry(self)
        self.entry.grid(row=3, column=0, sticky='WN')
        self.submitButton = tk.Button(self, text="Submit", command=self.loadInitialImage)
        self.submitButton.grid(row=4, column=0, sticky='WN')
        self.pictureWindow = tk.Canvas(self, width=600, height=300, bg="red")
        self.pictureWindow.create_text(300,150,fill="black",font="Times 20 italic bold", text="No Image Selected")
        self.pictureWindow.grid(row=5, column=0, columnspan=10)

    def loadInitialImage(self):
        self.im = Image.open(self.entry.get())
        self.img= ImageTk.PhotoImage(Image.open(self.entry.get()))
        sizeOfNewImage = self.im.size
        self.pictureWindow = tk.Canvas(self, width=sizeOfNewImage[0], height=sizeOfNewImage[1])
        self.pictureWindow.grid(row=5, column=0, columnspan=10)
        self.pictureWindow.create_image(0,0,image=self.img, anchor='nw')
        self.loadChoices()

    def loadImage(self):
        self.img = ImageTk.PhotoImage(self.im)
        sizeOfNewImage = self.im.size
        self.pictureWindow = tk.Canvas(self, width=sizeOfNewImage[0], height=sizeOfNewImage[1])
        self.pictureWindow.grid(row=5, column=0, columnspan=10)
        self.pictureWindow.create_image(0,0,image=self.img, anchor='nw')

    def loadChoices(self):
        Label(self, text="Please Click on one of the choices below", font="Times 20 bold").grid(row=6, column=0,columnspan=8)
        self.mirrorButton= tk.Button(self, text="Mirror", command=self.mirrorImage).grid(row=7, column=0, sticky='N')
        self.grayButton= tk.Button(self, text="GrayScale", command=self.grayImage).grid(row=7, column=1, sticky='N')
        self.flipButton= tk.Button(self, text="Flip", command=self.flipImage).grid(row=7, column=2, sticky='N')
        self.rotateButton= tk.Button(self, text="Rotate", command=self.rotateImage).grid(row=8, column=0, sticky='N')
        self.enlargeButton= tk.Button(self, text="Enlarge", command=self.enlargeImage).grid(row=8, column=1, sticky='N')
        #Need to finish Crop
        self.cropButton= tk.Button(self, text="Crop").grid(row=8, column=2, sticky='N')

        self.redButton= tk.Button(self, text="Red Scale", command=self.redImage).grid(row=9, column=0, sticky='N')
        self.blueButton= tk.Button(self, text="Blue Scale", command=self.blueImage).grid(row=9, column=1, sticky='N')
        self.greenButton= tk.Button(self, text="Green Scale", command=self.greenImage).grid(row=9, column=2, sticky='N')
        self.jumbleButton= tk.Button(self, text="Jumble", command=self.jumbleImage).grid(row=10, column=0, sticky='N')
        self.saveButton= tk.Button(self, text="Save", command=self.savePicture).grid(row=10, column=1, sticky='N')
        self.exitButton= tk.Button(self, text="Exit", command=self.destroy).grid(row=10, column=2, sticky='N')

    def mirrorImage(self):
        self.im = mirror(self.im)
        self.loadImage()

    def grayImage(self):
        self.im = gray(self.im)
        self.loadImage()

    def flipImage(self):
        self.im = flip(self.im)
        self.loadImage()

    def enlargeImage(self):
        self.im = enlarge(self.im)
        self.loadImage()

    def rotateImage(self):
        self.rotateInputLabel = tk.Label(self, text="Please enter either 90, 180, or 270", font="Time 10 bold").grid(row=6, column=5)
        self.rotateEntry = tk.Entry(self)
        self.rotateEntry.grid(row=7, column=5)
        self.rotateInputButton = tk.Button(self, text="Submit", command=self.rotate).grid(row=7, column=6)

    def rotateImage(self):
        print(self.rotateEntry.get())
        self.im = rotate(self.im, int(self.rotateEntry.get()))
        self.loadImage()

    def redImage(self):
        self.im = red(self.im)
        self.loadImage()

    def blueImage(self):
        self.im = blue(self.im)
        self.loadImage()

    def greenImage(self):
        self.im = green(self.im)
        self.loadImage()

    def jumbleImage(self):
        self.im = jumble(self.im)
        self.loadImage()

    def savePicture(self):
        self.im.save("Output.jpg")


startGUI = gui()
startGUI.mainloop()

'''
    if choice == "1":
        im = flip(pixels, size)
    elif choice == "2":
        choice = int(raw_input("Choose what degree to rotate (90, 180, or 270): "))
        im = rotate(im,choice)
    elif choice == "3":
        im = mirror(im)
    elif choice == "4":
        im = gray(im)
    elif choice == "5":
        im = enlarge(im)
    elif choice == "6":
        xStart = int(raw_input("Choose starting x coordinant to crop: "))
        xEnd = int(raw_input("Choose ending x coordinant to crop: "))
        yStart = int(raw_input("Choose starting y coordinant to crop: "))
        yEnd = int(raw_input("Choose ending y coordinant to crop: "))
        im = crop(im,xStart, xEnd, yStart, yEnd)
    elif choice == "7":
        im = red(im)
    elif choice == "8":
        im = blue(im)
    elif choice == "9":
        im = green(im)
    elif choice == "10":
        im = jumble(im)
    elif choice == "0":
        menu = False
'''
