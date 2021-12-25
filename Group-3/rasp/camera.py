import requests
import string
import random
import os
import time
from datetime import datetime as dt
from picamera import PiCamera

def takePic():
    camera = PiCamera();
    camera.resolution = (2592,1944)
    camera.brightness = 60
    camera.zoom = (0.3, 0.3, 1.0, 1.0)

    st = dt.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
    img = './hey/lot-1-' + st + '.png'
    print('Capturing image')
    camera.capture(img)
    print('Image captured ' + img)
    camera.close()

    return img

def sendPic(img):
    #url = 'http://192.168.0.117/lataaja.php'
    url = 'http://kvp0.ddns.net/lataaja.php'
    #url = 'https://www.ipt.oamk.fi/linux183/upload.php'

    files = {'image': open(img, 'rb')}
    response = requests.post(url, files=files)
    print(response.text)

    #cmd = "rm " + img
    #os.system(cmd)     

def main():
    while(True):
        img = takePic()
        sendPic(img)

        return(0)
        time.sleep(20)

if __name__ == "__main__":
    main()
