import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

while(cap.isOpened()):
    succes,img = cap.read()
    cvtimage = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = pose.process(cvtimage)

    if result.pose_landmarks:
        mpDraw.draw_landmarks(img,result.pose_landmarks, mpPose.POSE_CONNECTIONS)
    
    cv2.imshow("stream",img)

    if cv2.waitKey(1) == 113:
        break
    
