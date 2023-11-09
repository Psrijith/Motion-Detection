# Motion-Detection
Motion Detection and Tracking Using Opencv Contours
Project Overview:
The goal of this project is to detect and track movements in a video. It identifies changes between consecutive frames to highlight areas where motion occurs. The project involves the following steps:

Video Input: It starts by reading a video file ('testvideo.mp4') using OpenCV's VideoCapture function.

Motion Detection: The code processes each frame of the video to detect movement using the following techniques:

Frame Differencing: Calculates the absolute difference between two consecutive frames to identify regions where movement occurs.
Thresholding: Converts the difference image to a binary image by applying a threshold.
Contour Detection: Finds contours in the thresholded image. Contours represent areas where significant changes have occurred between frames.
Counting Movements: It counts the number of contours found in each frame, considering each contour as a movement detected in the video.

Visual Display: Displays the original video frames with highlighted contours where movement is detected. Additionally, it showcases the count of movements on the video frames using cv2.putText().

User Interaction: The code runs in a loop and continuously displays the video frames. The loop can be exited by pressing the 'q' key, allowing the user to stop the video and close the display window.

Possible Extensions or Use Cases:
Security Systems: This method could be used in security systems for monitoring and detecting movement in surveillance videos.
Activity Monitoring: It can be applied to monitor activity levels in specific areas captured by video.
Automated Alerts: It could trigger alerts or notifications when unexpected movements are detected.
The project provides a foundation for further development, such as integrating it into a more complex system or interface for specific applications related to motion detection and tracking in video streams. 
 # Steps to Run the Code:
  Install required libraries
  Save Code: Copy the provided Python code and save it as motion_detection.py.
  Open Terminal: Access the directory containing motion_detection.py.
  Execute Code: python motion_detection.py  
  Interaction: The video starts; press 'q' to exit and stop the script.

source = https://youtu.be/MkcUgPhOlP8?feature=shared
