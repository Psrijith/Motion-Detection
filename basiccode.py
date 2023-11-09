import cv2
import numpy as np

# Open the video file
cap = cv2.VideoCapture('testvideo.mp4')

while cap.isOpened():
    # Read the video frame by frame
    ret, frame = cap.read()
    # ret indicates whether a frame was successfully read
    # Check if a frame is successfully read
    if not ret:
        break  # If no frame is read, exit the loop

    # Display the frame in a window titled "inter"
    cv2.imshow("BASIC CODE TO RUN A VIDEO , Q TO EXIT", frame)

    # Wait for 40 milliseconds for a key to be pressed (imp)
    key = cv2.waitKey(40)

    # Check if the pressed key is 'q' (ASCII value 113)
    if key == ord('q'):
        break  # If 'q' is pressed, exit the loop

# Close all OpenCV windows
cv2.destroyAllWindows()

# Release the video capture resources
cap.release()
