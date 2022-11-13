from flask import Flask,render_template, send_file, request
import cv2
import os
import threading
import time


app= Flask(__name__)
@app.route('/')
def index():
  try:
    return render_template("index.html", image_file='static/default.jpg', disable=True, msg="")
  except:
    return "<h1>Sorry, Something Went Wrong. Please Try Again Later<h1>"


