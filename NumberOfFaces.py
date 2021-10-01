import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_face_detection.FaceDetection()

cap = cv2.VideoCapture(0)
while True:
    success, image = cap.read()
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(imgRGB)
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(image, detection)
            cv2.putText(image, "Number of faces detected : " + str(len(results.detections)),(10,70),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255), 2)  
    else:
         cv2.putText(image, "No faces detected",(10,70),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255), 2)   

    cv2.putText(image, "Press 'x' to quit",(10,470),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255), 2)                  
    cv2.imshow("Face Detection", image)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    