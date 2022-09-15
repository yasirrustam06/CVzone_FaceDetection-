import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector
face_detector = FaceDetector(minDetectionCon=0.5)

img =cv2.imread("FaceMesh.jpg")

Image,Faces = face_detector.findFaces(img)

if Faces:
    print(Faces[0])


cv2.imwrite("face_detection.jpg",Image)

cv2.imshow("Image",Image)
cv2.waitKey(0)
cv2.destroyAllWindows()
