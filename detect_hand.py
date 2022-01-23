'''
enter 
env/Scripts/activate
press q to quit
'''
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
solutions_hands=mp.solutions.hands
hands=solutions_hands.Hands()
mpdraw=mp.solutions.drawing_utils

while True:
    ret, img = cap.read()
    if ret:
        img_height=img.shape[0]
        img_width=img.shape[1]
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result=hands.process(imgRGB)
        if result.multi_hand_landmarks:
            for handlms in  result.multi_hand_landmarks:
                mpdraw.draw_landmarks(img,handlms,solutions_hands.HAND_CONNECTIONS)
                for i, lm in enumerate(handlms.landmark):
                    xPos=int(lm.x*img_width)
                    yPos=int(lm.y*img_height)
                    #print(i,xPos,yPos)
                    cv2.putText(img,str(i),(xPos-25,yPos+5),cv2.FONT_HERSHEY_SIMPLEX,0.4,(1650,40,0),2)
        cv2.imshow('handtracking',img)
    if cv2.waitKey(1)==ord('q'):
        break