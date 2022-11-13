from flask import Flask,render_template, send_file, request
import cv2
import os
import threading
import time


app= Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")



