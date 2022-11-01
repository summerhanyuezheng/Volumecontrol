from turtle import width
import cv2
import mediapipe as mp
import math


mp_hands = mp.solutions.hands
draw = mp.solutions.drawing_utils
#create a hand object
hands = mp_hands.Hands()

#passed in 1 becoz 1 want to use my second webcam
#variable capture has all the frames that's captured
capture = cv2.VideoCapture(0)
while True:
    #variable "image" has each frame
    value,image = capture.read() #a tuple
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # Print handedness and draw hand landmarks on the image.
    print(results.multi_hand_landmarks)
    if (results.multi_hand_landmarks):
        for handlandmarks in results.multi_hand_landmarks:
            for finger_id,landmark_co in enumerate(handlandmarks.landmark):
                #print(finger_id,landmark_co)
                height,width,channel = image.shape
                cx,cy = int(landmark_co.x * width), int(landmark_co.y * height)
                #print(finger_id,cx,cy)
                #4 means thumb, 8 is index finger
                if finger_id == 4:
                    cv2.circle(image,(cx,cy),30,(255,0,255),cv2.FILLED)
                    thumb_pixel_x,thumb_pixel_y = cx,cy
                if finger_id == 8:
                    cv2.circle(image,(cx,cy),30,(255,0,255),cv2.FILLED)
                    index_pixel_x,index_pixel_y = cx,cy
                    cv2.line(image,(thumb_pixel_x,thumb_pixel_y), (index_pixel_x,index_pixel_y),(0,255,0),9)
                    #finding the distance
                    distance = math.sqrt((index_pixel_x - thumb_pixel_x) ** 2 + (index_pixel_y - thumb_pixel_y) ** 2)
                    print(distance)







            draw.draw_landmarks(image, handlandmarks,mp_hands.HAND_CONNECTIONS) 
    cv2.imshow('Image capture', image)
    # a if statement for "pressing esc to exit the loop"
    if cv2.waitKey(1) & 0xFF == 27:
        break
#release capture object that's recurringly hold so it doesn't keep using my camera after while loop
capture.release()
cv2.destroyAllWindows()