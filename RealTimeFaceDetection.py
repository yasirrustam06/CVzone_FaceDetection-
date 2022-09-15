import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector
face_detector = FaceDetector(minDetectionCon=0.5)
cap = cv2.VideoCapture(0)
while True:
    ret ,img = cap.read()

    image,faces = face_detector.findFaces(img)
    if faces:
        print(faces[0])
    cv2.imshow("Image",image)
    if cv2.waitKey(1)  & 0xFF == ord("Q"):
        break


cap.release()
cv2.destroyAllWindows()
