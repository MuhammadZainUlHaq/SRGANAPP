from flask import Flask,render_template, send_file, request
import cv2
import os
import threading
import time

app = Flask(__name__)

time_tracker = dict()

download_file = None
download_path = None
super_res = cv2.dnn_superres.DnnSuperResImpl_create()

@app.route('/')
def index():
    try:
        return render_template("index.html", image_file = 'static/default.jpg', disable = True, msg = "")
    except:
        return "<h1>Sorry, Something Went Wrong. Please Try Again Later<h1>"

@app.route('/download')
def download():

    try:
        global download_file, download_path
        return send_file(download_path ,as_attachment= True,download_name= download_file)
    except:
        return "<h1>Sorry, Something Went Wrong. Please Try Again Later<h1>"

@app.route('/',methods=['GET','POST'])
def convert():
    try:
        global download_file, download_path,time_tracker

        print('convert work')
        if 'client_file' in request.files:
            file = request.files['client_file']
            file_name = file.filename
            format_list = ['jpg', 'jpeg', 'png', 'jp2', 'jpe', 'tiff', 'tif', 'bmp', 'pbm', 'pgm', 'ppm', 'sr', 'ras']
            file_str = file_name.split('.')[-1]

            if file_name == '':
                print('No file selected')
                img_file = 'static/default.jpg'
                disable = True
                msg = "Please select an image file to proceed"

            elif file_str.lower() not in format_list:
                print('File format not supported')
                img_file = 'static/default.jpg'
                disable = True
                msg = "File format not supported"

            else:
                file.save('static/user_file/' + file_name)
                img = cv2.imread('static/user_file/' + file_name)
                img_file = 'static/user_file/' + file_name

                selected_upscale = request.form.get('upscale')

                if selected_upscale == '2x':
                    super_res.readModel('ESPCN_x2.pb')
                    super_res.setModel('espcn', 2)
                elif selected_upscale == '3x':
                    super_res.readModel('ESPCN_x3.pb')
                    super_res.setModel('espcn', 3)
                else:
                    super_res.readModel('ESPCN_x4.pb')
                    super_res.setModel('espcn', 4)

                espcn_img = super_res.upsample(img)
                cv2.imwrite('static/user_file/deep' + file_name, espcn_img)

                download_file = 'deep_' + file_name
                download_path = 'static/user_file/deep' + file_name

                #time_tracker[file_name] = [time.time(),time.time()]
                #time_tracker['deep'+file_name] = [time.time(),time.time()]

                disable = False
                msg = " "

        else:
            print('No file part. app error.')
        return render_template('index.html', image_file=img_file, disable=disable,msg=msg)

    except:
        return "<h1>Sorry, Something Went Wrong. Please Try Again Later<h1>"

'''
def apprun():
    global app
    app.run()

def cleaner():
    global time_tracker
    while True:
        key_list = list()
        for k,v in time_tracker.items():
            key_list.append(k)
            tim_diff = abs(time.time() - v[0])
            time_tracker[k][1] = tim_diff

        for key in key_list:
            tim_diff = time_tracker[key][1]
            if tim_diff > 2500.0:
                del time_tracker[key]
                os.remove('static/user_file/'+key)
        key_list = []
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=cleaner)
    t1.start()
    apprun()
'''




# this is how button not from form can call a function
# <button onclick="location.href='{{ url_for('download') }}'" id="download" disabled>DOWNLOAD</button>