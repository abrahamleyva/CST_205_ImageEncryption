import flask
from flask import *
import os
from PIL import Image
import math
import time

app = flask.Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return flask.render_template("upload.html")
@app.route('/desition')
def desition():
    return flask.render_template("desition.html")
@app.route('/encrypt')
def encrypt():
    return flask.render_template("encrypt.html")
@app.route('/decrypt')
def decrypt():
    return flask.render_template("decrypt.html")
@app.route('/complete')
def complete():
    return flask.render_template("complete.html")
    
@app.route("/desition", methods = ['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'static/')
    print(target)
    
    if not os.path.isdir(target):
        os.mkdir(target)
    
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, 'image.png'])
        print(destination)
        file.save(destination)
    return render_template("desition.html")
    
@app.route("/encrypt", methods = ['POST'])
def runEncrypt():
    start_timer = time.time()
    
    img = Image.open("static/image.png")
    
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
    
    img.save("static/fimage.png")
    
    print("Done!")
    
    print("--- %s seconds ---" % (time.time() - start_timer))
    return render_template("encrypt.html")
@app.route("/decrypt", methods = ['POST'])
def runDecrypt():
    start_timer = time.time()
    
    img = Image.open("static/image.png")
    
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
                
    img.save("static/fimage.png")
    
    
    print("Done!")
    
    print("--- %s seconds ---" % (time.time() - start_timer))
    return render_template("decrypt.html")
@app.route("/complete", methods = ['POST'])
def runComplete():
    print("Hello")
    return render_template("complete.html")

if __name__ == "__main__":    
    app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0')
    )

app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0')
)