import cv2 as cv
import time
import os


def getNewID():
    home_path = os.getcwd()
    os.chdir("dataset/temp")

    while True:
        ID = input('Please type your ID: ')
        print('Your ID: ' + ID)
        confirm = input('Confirm ? [y/n] ')
        if confirm=='y' or confirm=='Y':
            break

    if not os.path.exists(ID):
        os.mkdir(ID)
    os.chdir(ID)

    cap = cv.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    timeout = time.time() + 5
    counter=0
    while True:
        ret, frame = cap.read()
        frame = cv.flip(frame,1)
        cv.imshow('Webcam', frame)

        img = "{}_{:04d}.png".format(ID,counter)
        cv.imwrite(img, frame)
        counter += 1
        k = cv.waitKey(30)&0xff
        if k==27 or time.time()>timeout:
            break

    cap.release()
    cv.destroyAllWindows()
#    os.chdir(home_path)
    return ID


