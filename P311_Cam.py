# capture image from nano kit caera and save file for viewing

import cv2

# Replace with the camera device ID (typically 0 for CSI camera)
#pip list

camera_id = 0

# Initialize the video capture object
cap = cv2.VideoCapture(camera_id)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video capture object")
    exit(1)

# Capture a frame
ret, frame = cap.read()

# Check if frame captured successfully
if not ret:
    print("Error capturing frame")
    exit(1)

# Save the frame as an image
cv2.imwrite("captured_image.jpg", frame)

# Release the video capture object
cap.release()

print("Image captured and saved as captured_image.jpg")
