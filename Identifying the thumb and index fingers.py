import cv2
import math
import mediapipe as mp
mp_hands=mp.solutions.hands
hands=mp_hands.Hands()
draw=mp.solutions.drawing_utils
capture=cv2.VideoCapture(0)
while True:
    value,image=capture.read()
    rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    processed_image=hands.process(rgb_image)
    print(processed_image.multi_hand_landmarks)
    if(processed_image.multi_hand_landmarks):
        for handlandmark in processed_image.multi_hand_landmarks:
            for finger_id,landmark_co in enumerate(handlandmark.landmark):
               #print(finger_id,landmark_co)
                height,width,channel=image.shape
                cx,cy=int(landmark_co.x * width),int(landmark_co.y*height)
                #print(finger_id,cx,cy)
                if finger_id==4:
                    cv2.circle(image,(cx,cy),30,(255,0,255),cv2.FILLED)
                    tpx,tpy=cx,cy
                if finger_id==8:
                    cv2.circle(image,(cx,cy),30,(255,0,255),cv2.FILLED)
                    ipx,ipy=cx,cy
                    cv2.line(image,(tpx,tpy),(ipx,ipy),(0,255,0),9)
                    distance=math.sqrt((ipx-tpx)**2+(ipy-tpy)**2)
                    print(distance)
            draw.draw_landmarks(image,handlandmark,mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Image capture',image)
    if cv2.waitKey(1) & 0xFF==27:
        break
capture.release()
cv2.destroyAllWindows()

 