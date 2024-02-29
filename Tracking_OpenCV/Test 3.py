import cv2
import mediapipe as mp
import time

cap1 = cv2.VideoCapture()


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap1.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    cv2.imshow("Image", img)
    cv2.waitKey(1)