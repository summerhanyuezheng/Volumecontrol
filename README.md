# Volume control by hand tracking
# Project Description:  
The project uses a web camera to detect hands. It measures the distance between the thumb and index finger. The device’s volume changes accordingly based on how the distance changes.
# Technology used:
- Anaconda: I personally had trouble running the program on Mac terminal without using conda. but if yours running ok, then this step is not needed.
- opencv : OpenCV-Python is a library of Python bindings designed to solve computer vision problems
- MediaPipe : a machine learning solution library
- Osascript
- numpy : in this particular project, the library used to map the distance between two fingers to the volume
# Installation Instruction (For Mac)
- opencv : `pip install opencv-python`
- mediapipe : `pip install mediapipe`
- osascript : `pip install osascript`
- numpy : `pip install numpy`
# Method used
### for cv2 library:
  - `.VideoCapture()`
  - `.imshow()` to display an image in a window
  - `.waitKey()`
  - `.destroyAllwindows()`
  - `.cvtColor()` to convert an image from one color space to another, in this project it's converting BGR to RGB
  - `.circle()`
  - `.FILLED`
  - `.line()`
### for mediapipe library(python solution API):
  - `.hands`
  - `.Hands()`
  - `.multi_hand_landmarks`
  - `.drawing_utils`
  - `.draw_landmarks`
  - `.HAND_CONNECTIONS`
  - `.shape`
  - `.landmark`
### for numpy library:
  - `.interp()`
### for osascript library:
  - `.osascript()`
# Video demo:
- video demo1 for the project (https://www.youtube.com/watch?v=3MSKSwdgQj0)
- video demo2 for the project (https://www.youtube.com/watch?v=_MA4ICLP1-A)

  
# notes for myself
  - when you need to capture something from webcam, you have to create a VideoCapture object. **Videocapture()** is a built-in method in cv2.

  - ![image](https://mediapipe.dev/images/mobile/hand_landmarks.png)
