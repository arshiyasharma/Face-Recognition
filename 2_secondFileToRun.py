import cv2
import os
import numpy as np

def labels_for_training_data(directory):
    faces = []
    facesId = []
    for path,subdirectory,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("Skipping System File")
                continue
            id = os.path.basename(path)
            img_path = os.path.join(path,filename)
            print("Image Path:",img_path)
            print("Id",id)
            test_img = cv2.imread(img_path)
            if test_img is None:
                print("Image Not Loaded Properly")
                continue
            faces_rect,gray_img = faceDetection(test_img)
            if len(faces_rect)!=1:
                continue   # skip in case of multiple or no faces
            (x,y,w,h) = faces_rect[0]
            face_image = gray_img[y:y+h,x:x+w]
            faces.append(face_image)
            facesId.append(int(id))
    return faces,facesId

def faceDetection(test_img):
    gray_img = cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("face.xml")
    faces = face_cascade.detectMultiScale(gray_img)
    return faces,gray_img

def train_classifier(faces,faceId):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces,np.array(faceId))
    return face_recognizer

faces,facesId = labels_for_training_data("samples")
face_recognizer = train_classifier(faces,facesId)
face_recognizer.write("MyFaceModel.yml")
print("Model Trained Successfully")
