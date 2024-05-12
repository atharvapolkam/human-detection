import cv2
import pandas as pd
from ultralytics import YOLO

# Initialize YOLO model
model = YOLO('yolov8s.pt')

# Function to print RGB values when mouse moves over frame
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

# Create window and set mouse callback
cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

# Open video capture (assuming webcam)
cap = cv2.VideoCapture('peoplewalking.mp4')

# Read class names from file
with open("coco.txt", "r") as my_file:
    data = my_file.read()
    class_list = data.split("\n")

count = 0

# Main loop for video processing
while True:    
    # Read frame from camera
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 2 != 0:
        continue
    # Resize frame
    frame = cv2.resize(frame, (1020, 500))

    # Make predictions using YOLO model
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
             
    # Iterate over detected objects and draw bounding boxes
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]
        if 'person' in c:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, str(c), (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
        
    # Display frame
    cv2.imshow("RGB", frame)
    
    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    # Exit loop if 'q' key is pressed
    if key == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()
