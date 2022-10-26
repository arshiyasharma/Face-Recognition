import cv2

cam = cv2.VideoCapture(0)
n1=input('Enter name of the first person: ')
n2=input('Enter name of the second person: ')
names = {

    1 : n2,
    0 : n1
}
face_cascade = cv2.CascadeClassifier("face.xml")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("MyFaceModel.yml")
while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for x, y, w, h in faces:
        single_face = gray[x:x+w, y:y+h]
        id, confidence = face_recognizer.predict(gray)
        print(id, confidence)

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
        predicted_name = names[id]

        if confidence > 70:
            cv2.putText(img, predicted_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()