#!/usr/bin/env python
import os
import glob
import requests as rq


def getLatestFile():
    list_of_files = glob.glob('./uploads/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file
def countCars():
    counter = 0
    with open('result','r') as file:
        for line in file:
            for word in line.split():
                if word == "car:":
                    counter += 1
    print(counter)
    return counter
def postTheResults():
    insert_url = 'https://www.ipt.oamk.fi/linux183/insert.php'
    upload_url = 'https://www.ipt.oamk.fi/linux183/upload.php'

    payload = {
            'paikat':countCars(),
            'submitted':True,
            }

    files = {'image': open(getLatestFile(), 'rb')}

    response = rq.post(upload_url, files=files)
    print("upload",end=" ")
    print(response.status_code)

    response = rq.post(insert_url, data=payload)
    print("insert",end=" ")
    print(response.status_code)


def main():
    os.system("./darknet detect cfg/yolov4.cfg yolov4.weights {} -ext_output > result".format(getLatestFile()))

    postTheResults()

if __name__ == "__main__":
    main()
