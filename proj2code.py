from PIL import Image
import os.path


def encryption(arr):
    arr = sorted(arr)
    if len(arr) == 0:
        return None
    else:
        return arr

path = "Images"
num_files = len([i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))]) - 1

ImageList = [None] * num_files

for i in range(0, num_files):
    ImageList[i] = Image.open("Images/" + str(i+1) + ".png")

width, height = ImageList[0].size

ImageList[0].save("Images/encryptedImage.png")
finalTemp = Image.open("Images/encryptedImage.png")
encryptedImage = finalTemp


Red = 0
Green = 0
Blue = 0

redPixelList = [None] * num_files
greenPixelList = [None] * num_files
bluePixelList = [None] * num_files

myPixels = [None] * num_files

for i in range(0, num_files):
    myPixels[i] = ImageList[i].load()
    

for y in range(0, height):
    for x in range(0, width):
        for j in range(0, num_files):
            pix = myPixels[j]
            redPixelList[j] , greenPixelList[j], bluePixelList[j] = pix[x,y]
        
        Red = encryption(redPixelList)
        Green = encryption(greenPixelList)
        Blue = encryption(bluePixelList)
        encryptedImage[x,y] = (Red, Green, Blue)
        
finalTemp.save('Images/encryptedImage.png')