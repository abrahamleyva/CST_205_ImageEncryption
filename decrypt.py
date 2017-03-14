from PIL import Image
import math
import time

start_timer = time.time()

img = Image.open("Encyrpt50.png")

arr = img.load() #pixel data stored in this 2D array

def rot(A, n, x1, y1): #this is the function which rotates a given block
    temple = []
    for i in range(n):
        temple.append([])
        for j in range(n):
            temple[i].append(arr[x1+i, y1+j])
    for i in range(n):
        for j in range(n):
            arr[x1+i,y1+j] = temple[n-1-i][n-1-j]

xres, yres = img.size
BLKSZ = 50 #blocksize

for i in range(2, BLKSZ+1):
    for j in range(int(math.floor(float(xres)/float(i)))):
        for k in range(int(math.floor(float(yres)/float(i)))):
            rot(arr, i, j*i, k*i)
for i in range(3, BLKSZ+1):
    for j in range(int(math.floor(float(xres)/float(BLKSZ+2-i)))):
        for k in range(int(math.floor(float(yres)/float(BLKSZ+2-i)))):
            rot(arr, BLKSZ+2-i, j*(BLKSZ+2-i), k*(BLKSZ+2-i))
            
img.save("Decrypt"+str(BLKSZ)+".png")


print("Done!")

print("--- %s seconds ---" % (time.time() - start_timer))