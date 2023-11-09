import cv2
import numpy as np

# Open the video file
cap = cv2.VideoCapture('testvideo.mp4')

# Read two initial frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Find the absolute difference between two consecutive frames
    diff = cv2.absdiff(frame1, frame2)

    # Convert the difference image to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply a threshold to create a binary image
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Dilate the thresholded image to fill gaps
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours in the dilated image
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original frame
    cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    # Display the frame with drawn contours
    cv2.imshow("Demo", frame1)

    # Update frames for the next iteration
    frame1 = frame2
    ret, frame2 = cap.read()

    # Check for the 'q' key to quit the loop
    key = cv2.waitKey(40)
    if key == ord('q'):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()

# Release the video capture resources
cap.release()
