

---

# Real-time Human Detection with YOLOv8

This Python script utilizes the YOLOv8 model for real-time object detection on a video stream.
It detects people in the video feed and draws bounding boxes around them.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- Pandas (`pd`)
- Ultralytics (`YOLO`)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place the `yolov8s.pt` and `coco.txt` files in the same directory as the Python script.
2. Run the Python script:
   ```
   main.py
   ```
3. A window will open displaying the video feed with bounding boxes around detected people.
4. Move the mouse over the video feed to print RGB values of the pixels.

## Keyboard Controls

- Press `q` to quit the program.

## Notes

- The script assumes the input video is named `peoplewalking.mp4`. You can change this by modifying the `VideoCapture` line in the script.
- Ensure your webcam is correctly configured if you intend to use it instead of a video file.

--- 
