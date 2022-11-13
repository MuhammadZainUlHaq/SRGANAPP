from flask import Flask,render_template, send_file, request
import cv2
import os
import threading
import time


app= Flask(__name__)
@app.route('/')
def index():
    return render_template("new.html", image_file = 'static/default.jpg', disable = True, msg = "")



@app.route('/',methods=['GET','POST'])
def convert():
    return render_template("new.html",disable = True)



