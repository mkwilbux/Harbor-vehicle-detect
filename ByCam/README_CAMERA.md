# 🚀 Vehicle Recognition Using Webcam or External Camera (YOLOv8)

This project detects vehicles **in real-time using a webcam** or an **external camera** with **YOLOv8 and OpenCV**.

## 📌 Installation Guide

### **Step 1: Install Python (If Not Installed)**
Ensure you have **Python 3.8+** installed. Check your Python version:

```bash
python3 --version
```

If you don’t have it, [download Python](https://www.python.org/downloads/) and install it.

### **Step 2: Install Required Dependencies**
Run the following command to install OpenCV, YOLO, and other necessary libraries:

```bash
pip install ultralytics opencv-python numpy
```

### **Step 3: Ensure Your Camera is Working**
Run this command to **test if your webcam is detected**:

```bash
python -c "import cv2; print(cv2.VideoCapture(0).isOpened())"
```

If **False**, check your **camera connection or try using `cv2.VideoCapture(1)`**.

## 📌 Running the Script

1. **Save the Python script** as `vehiclerec-cam.py`.
2. **Run the script**:
   ```bash
   python3 vehicle_recognition_camera.py
   ```
3. **Press 'q' to exit** the detection window.

## 📌 Troubleshooting

### ❌ **Issue: "Could not open webcam."**
- Ensure your **webcam is connected** and working.
- Try changing `cv2.VideoCapture(0)` to:
  ```python
  cap = cv2.VideoCapture(1)  # Use external camera
  ```

### ❌ **Issue: Bounding Boxes Not Showing**
- Try using a **larger YOLO model**:
  ```python
  model = YOLO("yolov8x.pt")
  ```
- Lower the confidence threshold:
  ```python
  results = model(frame_rgb, conf=0.02, iou=0.5)
  ```
