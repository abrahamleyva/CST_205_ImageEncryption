import flask
from flask import *
import os

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
    print("Hello")
    return render_template("encrypt.html")
@app.route("/decrypt", methods = ['POST'])
def runDecrypt():
    print("Hello")
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