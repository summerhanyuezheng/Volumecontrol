import cv2
#passed in 1 becoz 1 want to use my second webcam
#variable capture has all the frames that's captured
capture = cv2.VideoCapture(1)
while True:
    value,image = capture.read() #a tuple
    cv2.imshow('Image capture', image)
    # a if statement for "pressing esc to exit the loop"
    if cv2.waitKey(1) & 0xFF == 27:
        break
#release capture object that's recurringly hold so it doesn't keep using my camera after while loop
capture.release()
cv2.destroyAllWindows()