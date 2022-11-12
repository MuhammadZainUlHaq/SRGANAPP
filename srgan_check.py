import os
import time
import threading

images = os.listdir('static/user_file')
print(images)

def run():
    for img in images:
        os.remove('static/user_file/'+img)

t1 = threading.Thread(target=run)
t1.start()

print(time.time())
time.sleep(2.5)
print(time.time())