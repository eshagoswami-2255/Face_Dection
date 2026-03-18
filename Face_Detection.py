import cv2
import cv2.data
from random import randint

modelPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml" 
model = cv2.CascadeClassifier(modelPath)

camera = cv2.VideoCapture(0)

while True:
    status, frame = camera.read()
    faces = model.detectMultiScale(frame, 1.3, 5)
    for face in faces:
        x, y, w, h = face
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("Faces", frame)
    if cv2.waitKey(1) == ord('q'):
        break