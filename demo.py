import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
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
    cv2.imshow('Image capture', image)
    # a if statement for "pressing esc to exit the loop"
    if cv2.waitKey(1) & 0xFF == 27:
        break
#release capture object that's recurringly hold so it doesn't keep using my camera after while loop
capture.release()
cv2.destroyAllWindows()