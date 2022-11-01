# Volume control by hand tracking
# Technology used:
- Anaconda: I personally had trouble running the program on Mac terminal without using conda. but if yours running ok, then this step is not needed.
- opencv : OpenCV-Python is a library of Python bindings designed to solve computer vision problems
- MediaPipe : a machine learning solution library
# Installation Instruction
- opencv : `pip install opencv-python`
- mediapipe : `pip install mediapipe`
# method used (from cv2 library)
## for cv2 library:
  - `VideoCapture()`
  - `imshow()` to display an image in a window
  - `waitKey()`
  - `destroyAllwindows()`
  - `cvtColor()` to convert an image from one color space to another, in this project it's converting BGR to RGB
## for mediapipe library(python solution API):
  - `.hands`
  - `.Hands()`
  - `.multi_hand_landmarks`
  - `.drawing_utils`
  - `.draw_landmarks`
  - `.HAND_CONNECTIONS`
  
# notes for myself
- when you need to capture something from webcam, you have to create a VideoCapture object. **Videocapture()** is a built-in method in cv2.
- ![image for connections between index and fingers](https://mediapipe.dev/images/mobile/hand_landmarks.png)
