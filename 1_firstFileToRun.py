import cv2


face_cascade = cv2.CascadeClassifier("face.xml")

def face_extracter(img):
    faces = face_cascade.detectMultiScale(img)
    for x, y, w, h in faces:
        global cropped_face
        cropped_face = img[x:x + w, y:y + h]
    return cropped_face


def collect_samples(person):
    cam = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = cam.read()
        if ret == True:
            if face_extracter(frame) is not None:
                count = count + 1
                face = cv2.resize(face_extracter(frame), (400, 400))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name_path = r'samples/' + str(person) + '/user' + str(count) + ".jpg"
                cv2.imwrite(file_name_path, face)
                cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Face Cropper", face)
            else:
                print("Face Not Found")
                pass
            if cv2.waitKey(1) == ord("q") or count == 500:
                break
    cam.release()
    cv2.destroyAllWindows()
    print("Collecting Samples Completed")


print('Taking first person samples.')
collect_samples(0)
print('Taking second person samples')
collect_samples(1)
