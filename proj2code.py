from PIL import Image
import os.path
from numpy import *
from pylab import imread, imsave

# def encryption(arr):
#     arr = sorted(arr)
#     if len(arr) == 0:
#         return None
#     else:
#         return arr
#         for int i in range(0, len(arr) -1):
            


path = "Images"
num_files = len([i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))]) - 1 #creating a path to get to the image

#ImageList = [None] * num_files

# for i in range(0, num_files):
#     ImageList[i] = Image.open("Images/" + str(i+1) + ".png")

img = Image.open("Images/Image.jpg") #save the image
width, height = img.size #get image size info



img.save("Images/encryptedImage.jpg") #save the encrytped image
finalTemp = Image.open("Images/encryptedImage.jpg")
encryptedImage = finalTemp


Red = 0
Green = 0 #initilize RGB values if we use them
Blue = 0

# redPixelList = [None] * num_files
# greenPixelList = [None] * num_files
# bluePixelList = [None] * num_files

myPixels = [None] * num_files #make a list of the pixels

# for i in range(0, num_files):
#     myPixels[i] = ImageList[i].load()
    

# for y in range(0, height):
#     for x in range(0, width):
#         for j in range(0, num_files):
#             pix = myPixels[j]
#             redPixelList[j] , greenPixelList[j], bluePixelList[j] = pix[x,y]
        
#         Red = encryption(redPixelList)
#         Green = encryption(greenPixelList)
#         Blue = encryption(bluePixelList)
#         encryptedImage[x,y] = (Red, Green, Blue)


imagePix = finalTemp.load() #Makes the new image able to be processes

print("Processing...") #tell the user it is working on the image

tempPix = imagePix

for y in range(0, height): #Goes through vertical pixels
    for x in range(0, width): #Goes through horizontal pixels
        if x % 2 == 0 and y % 2 == 0:
            tempPix[x, (y + 10) % height] = imagePix[x, y]
        elif x % 2 != 0 and y % 2 == 0:
            tempPix[x, (y - 20) % height] = imagePix[x, y]
        elif x % 2 == 0 and y % 2 != 0:
            tempPix[(x - 30) % width, y] = imagePix[x, y]
        else:
            tempPix[(x + 40) % width, y] = imagePix[x, y]

for y in range(0, height): #Goes through vertical pixels
    for x in range(0, width): #Goes through horizontal pixels
        if x % 2 == 0 and y % 2 == 0:
            tempPix[x, (y - 10) % height] = imagePix[x, y]
        elif x % 2 != 0 and y % 2 == 0:
            tempPix[x, (y + 20) % height] = imagePix[x, y]
        elif x % 2 == 0 and y % 2 != 0:
            tempPix[(x + 30) % width, y] = imagePix[x, y]
        else:
            tempPix[(x - 40) % width, y] = imagePix[x, y]

for y in range(0, height): #Goes through vertical pixels
    for x in range(0, width): #Goes through horizontal pixels
        if x % 2 == 0 and y % 2 == 0:
            tempPix[x, (y + 20) % height] = imagePix[x, y]
        elif x % 2 != 0 and y % 2 == 0:
            tempPix[x, (y + 40) % height] = imagePix[x, y]
        elif x % 2 == 0 and y % 2 != 0:
            tempPix[(x + 90) % width, y] = imagePix[x, y]
        else:
            tempPix[(x - 120) % width, y] = imagePix[x, y]

for y in range(0, height): #Goes through vertical pixels
    for x in range(0, width): #Goes through horizontal pixels
        if x % 2 == 0 and y % 2 == 0:
            tempPix[x, (y - 20) % height] = imagePix[x, y]
        elif x % 2 != 0 and y % 2 == 0:
            tempPix[x, (y - 40) % height] = imagePix[x, y]
        elif x % 2 == 0 and y % 2 != 0:
            tempPix[(x - 90) % width, y] = imagePix[x, y]
        else:
            tempPix[(x + 120) % width, y] = imagePix[x, y]





# def imshuffle(im, nx=0, ny=0):
#     for i in range(nx):
#         im = concatenate((im[:,0::2], im[:,1::2]), axis=1)
#     for i in range(ny):
#         im = concatenate((im[0::2,:], im[1::2,:]), axis=0)
#     return im

# def imunshuffle(im, nx = 0, ny = 0):
#     for i in range(nx):
#         im = split((im[:,0::2], im[:,1::2]), axis=1)
#     for i in range(ny):
#         im = split((im[0::2,:], im[1::2,:]), axis=0)
#     return im

# im1 = imread('Images/Image.jpg')
# #im2 = imread('mountain.jpg')

# imsave('Images/encryptedImage.jpg', imshuffle(im1, 7,7))
# imsave('Images/encryptedImage.jpg', imunshuffle(im1, (7,7))
#imsave('s_mountain.jpg', imshuffle(im2, 8,9))







imagePix = tempPix #finalize the changes
        

print("Complete!") #tells the user it is done
        
finalTemp.save('Images/encryptedImage.png')#saves the changes