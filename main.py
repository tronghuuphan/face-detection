from mtcnn import MTCNN
import cv2 as cv
import os
import video_capture
import shutil 


home_path = os.getcwd()
def draw_bounding_box(img, result):
    bounding_box= result[0]['box']
    cv.rectangle(img, (bounding_box[0], bounding_box[1]), (bounding_box[0]+bounding_box[2],bounding_box[1]+bounding_box[3]), (0,155,255), 2)
#    cv.imwrite('img.jpg',cv.cvtColor(img, cv.COLOR_RGB2BGR))

def crop_resize(img, result, filename, ID,  size=178):
    current_dir = os.getcwd()
    bounding_box = result[0]['box']
    crop_img = img[bounding_box[1]:bounding_box[1]+bounding_box[3], bounding_box[0]:bounding_box[0]+bounding_box[2]]
    resize_img = cv.resize(crop_img, (size,size), interpolation=cv.INTER_AREA)
    new_dir = os.path.join(home_path, 'dataset', ID)
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    os.chdir(new_dir)
    cv.imwrite(filename, resize_img)
    os.chdir(current_dir)

def delete_dir(ID):
    path = os.path.join(home_path, 'dataset/temp')
    os.chdir(path)
    shutil.rmtree(ID)
    os.chdir(home_path)

def detect_face():
    detector = MTCNN()
    for filename in os.listdir():
        img = cv.imread(filename)
        img_cvt = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        result = detector.detect_faces(img_cvt)
        if result == []:
            break
        print(result)
        crop_resize(img, result, filename, ID)
    delete_dir(ID) # delete ID folder and return to home_path


ID = video_capture.getNewID()
detect_face()
