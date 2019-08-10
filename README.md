# pypixelator

Caameron Nakasone and Sunanth Sakthivel</br>
Copyright © 2019 Caameron Nakasone and Sunanth Sakthivel

## Description:
pypixelator is a image altering program with a graphic user interface that has been written in Python.
the user will be prompted with several different features to manipulate the image. Features include changing the size, color, contrast, adding effects, pixelating portions, rotation and much more. Moreover, the user will be given the opportunity to chain several of these features by selecting any number of modifications to the desired image. Everytime a modification is made on the image, the sample image will be shown. Once the user has selected all their choices, the final image will be provided for the user to checkout all the modifications made.


The idea for this program started with figuring out how to just pixelate an image. We then quickly realized that we could do a lot more by going through the pixel values of an image and altering them in different ways. The first iteration of this program began with just a command line interface, however that has evolved into a graphical user interface that allows the user to see what exactly is being done to their image. Currently there are several features which allow the user to alter their image such as pixelate, crop, mirror, etc. with the ability to use multiple features on one image in succession. New features are also easily incorporated making this program easily expandable.

pypixelator works by leveraging a basic image library (pillow) that extracts dynamic images from different image files (i.e .png, .jpeg) and iterating through the respective pixels in order to alter the image as desired. The graphic user interface has been created using the Tkinter library in python.

## How to Build:
Make sure to have a working version of Python and PIP (currently we are using Python 2.7)
[Install PIP here](https://pip.pypa.io/en/stable/installing/)


Install [pillow](https://pypi.org/project/Pillow/2.2.2/)
```
python -m pip install Pillow
```
Install [image](https://pillow.readthedocs.io/en/3.1.x/reference/Image.html)
```
python -m pip install image
```
Install [numpy](https://www.numpy.org/)
```
python -m pip install numpy
```
Run main file on command line
```
python main.py
```

## How it works
A graphic user interface should pop up with an entry box for the path to the image and a submit button. Enter in the path to your image and click the submit button to see your image pop up on the screen. The choices on how to alter your image will also pop up below your picture, click on one of the options to apply that to your image, in some cases you will be asked for extra information on how/where you would like the altercation to take place. For example, rotate will need to know if you want to rotate your image 90, 180, or 270 degrees. Finally if you are satisfied with your image you can click on the save button which will save your file as Output.jpg in the current directory and then you can click the exit button to end the program.

## To Do
pypixelator is still only in its first version and a lot of work still needs to be done. There are a couple of issues which have been made on github to explain some of them. A more detailed list will be displayed below.

* Error Handling for images with wrong input
* A revert to original image button
* Clean up GUI and make it more user friendly
* Save multiple pictures
* Create more unit tests
* Integration tests
* Add more features...


## License Information
Licensed with MIT License. See [LICENSE](/LICENSE)
