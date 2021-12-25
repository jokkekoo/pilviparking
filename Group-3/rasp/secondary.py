import numpy as np
import cv2
import glob
import os

def latest():
    list_of_files = glob.glob('./pics/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def cap():
    video = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = video.read()
        cv2.imwrite("ppic.png",frame)
        result = False
    video.release()
    cv2.destroyAllWindows()

def con(interpolation=cv2.INTER_CUBIC):
    im1 = cv2.imread(latest())
    im2 = cv2.imread('ppic.png')

    im_list = [im1,im2]
    w_max = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_max, int(im.shape[0] * w_max / im.shape[1])), interpolation=interpolation)
            for im in im_list]
    cv2.imwrite('asdf.png', cv2.hconcat(im_list_resize))


def main():

    cap()
    con()

if __name__ == "__main__":
    main()
