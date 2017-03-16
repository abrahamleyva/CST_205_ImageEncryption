# Project: Image Encrypt and Decrypt
# Contributers: Abraham Medina, Ethan Ward, Bret Stine
# Class: CST 205-02 Spring 2017
# Date: March 16, 2017
# Abstract: This program allows the user to upload an image to a webpage and allows them to encrypt of decrypt the image.
# Contribution: Ethan and Bret both coded lines 47-79 of proj2Team230.py and Abraham worked on the rest of proj2Team230.py and the other files.
# Github: https://github.com/abrahamleyva/CST_205_ImageEncryption

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
@app.route('/decision')
def decision():
    return flask.render_template("decision.html")
@app.route('/encryptDecrypt')
def encryptDecrypt():
    return flask.render_template("encryptDecrypt.html")
    
@app.route("/decision", methods = ['POST'])
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
    return render_template("decision.html")
    
@app.route("/encryptDecrypt", methods = ['POST'])
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
    
    img.save("static/finalImage.png")
    
    return render_template("encryptDecrypt.html")

if __name__ == "__main__":    
    app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0')
    )

app.run(
    port = int(os.getenv('PORT', 8080)),
    host = os.getenv('IP', '0.0.0.0')
)