from PIL import Image
import os.path

path = "Images"
num_files = len([i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))]) - 1

ImageList = [None] * num_files

for i in range(0, num_files):
    ImageList[i] = Image.open("Images/" + str(i+1) + ".png")

width, height = ImageList[0].size

