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
        Label(self, text='Image Alterer',font="Times 20 bold").grid(row=0, column=3)
        self.winfo_toplevel().title("Image Alterer Version 0.1")
        self.winfo_toplevel().geometry("800x800")
        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=1)
        self.submitButton = tk.Button(self, text="Submit", command=self.loadImage)
        self.submitButton.grid(row=1, column=2)
        self.pictureWindow = tk.Canvas(self, width=300,height=300, bg="black")
        self.pictureWindow.create_text(150,150,fill="white",font="Times 20 italic bold", text="No Image Selected")
        self.pictureWindow.grid(row =1, column=4)


    def loadImage(self):
        print(self.entry.get())
        # self.im = Image.open(self.entry.get())
        self.img= ImageTk.PhotoImage(Image.open(self.entry.get()))
        self.pictureWindow.create_image(300,300, image=self.img)
        # self.size = self.im.size
        # self.pixels = self.im.load()



# root = Tk()
# root.title('Image Alterer Version 0.0')
# Label(root, text='File Path to Image').grid(row=0)
# e1= Entry(root)
# e1.grid(row=0, column=1)
# submitButton = Button(root, text="Submit", command=loadImage("tests/testPhotos/beach.jpeg"))
# submitButton.grid(row=0, column=2)
# root.mainloop()
startGUI = gui()
# startGUI.loadImage("tests/testPhotos/beach.jpeg")
startGUI.mainloop()


print("Here are the list of features available")
menu = True
while menu == True:
    print("1 : Flip")
    print("2 : Rotate")
    print("3 : Mirror")
    print("4 : GrayScale")
    print("5 : Enlarge")
    print("0 : Exit Program")
    choice = raw_input("Please enter in the number of the feature : ")

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
    elif choice == "0":
        menu = False

'''
Using size we can loop through all the pixels and manipulate them however we wish
'''
# for x in range(700):
#     pixels[x, 30] = (0,0,0)
# pixel_array = np.array(pixels, dtype=np.uint8)
# final_image = Image.fromarray(pixel_array)
# final_image.save("test.jpg")
im.save("test.jpg")
'''
Have to install cv2 using pip install opencv-python
and Pillow using pip install Pillow
'''
