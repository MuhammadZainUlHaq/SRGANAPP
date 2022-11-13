from flask import Flask,render_template, send_file, request
import cv2
import os
import threading
import time


app= Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", image_file = 'static/default.jpg', disable = True, msg = "")

@app.route('/download')
def download():
    return "nothing"

@app.route('/',methods=['GET','POST'])
def convert():
    return render_template("index.html")



