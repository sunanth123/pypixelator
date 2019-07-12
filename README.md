# pypixelator

Caameron Nakasone and Sunanth Sakthivel</br>
Copyright © 2019 Caameron Nakasone and Sunanth Sakthivel

## Description:
This command line program essentially will allow for image manipulation by changing different properties of its pixels. Moreover, by altering and changing the pixel layout of images there are a large array of features that can be implemented in order to perform the various preferences of the user. 

PyPixelator works by leveraging a basic image library (pillow) that extracts dynamic images from different image files (i.e .png, .jpeg) and iterating through the respective pixels in order to alter the image as desired. 

PyPixelator is a command line program that will take in an image file path as an argument and then the user will be prompted with several different features to manipulate the image. Features include changing the size, color, contrast, adding effects, pixelating portions, rotation and much more. Moreover, the user will be given the opportunity to chain several of these features by selecting any number of modifications to the desired image. Everytime a modification is made on the image, the sample image will be shown. Once the user has selected all their choices, the final image will be provided for the user to checkout all the modifications made. 

## How to Build:
Make sure to have a working version of Python and PIP
[Install PIP here](https://pip.pypa.io/en/stable/installing/)

Install [opencv-python](https://pypi.org/project/opencv-python/)
```
pip install opencv-python 
```

Install [pillow](https://pypi.org/project/Pillow/2.2.2/)
```
pip install Pillow
```

Run code
```
python pypixelator.py <path to image file>
```
## Operation of Code:

Program is run by: `python pypixelator <image path>`

User will then be prompted to select options to modify the image until they choose to exit: 

    What would you like to be done to your image?
    1 : Flip
    2 : Mirror
    3 : Grayscale
    4 : Rotate
    5 : Jumble
    6 : Enlarge
    7 : Pixelate
    8 : Crop
    0 : EXIT PROGRAM
    Enter in the number of the feature: 
    
## License Information
Licensed with MIT License. See [LICENSE](/LICENSE)
