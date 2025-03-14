# 🚀 Vehicle Recognition Using a Video Stream URL (YOLOv8)

This project detects vehicles in a **live video stream** using **YOLOv8 and OpenCV**.

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

### **Step 3: Find a Direct Video Stream URL**
1. Open the **traffic camera or live video page** in Chrome.
2. Press **F12** to open **Developer Tools**.
3. Go to the **Network tab** → Click **Media**.
4. Refresh the page (`Ctrl + R` or `Cmd + R`).
5. Look for a video file ending in **.m3u8, .mp4, or .mjpg**.
6. **Copy the URL** and test it in a browser.

## 📌 Running the Script

1. **Save the Python script** as `vehicle_recognition_url.py`.
2. **Replace `YOUR_EXTRACTED_URL`** in the script with your video URL.
3. **Run the script**:
   ```bash
   python3 vehicle_recognition_url.py
   ```
4. **Press 'q' to exit** the detection window.

## 📌 Troubleshooting

### ❌ **Issue: "Could not open video stream."**
- Ensure the **URL is correct** and works in a browser.
- Try **using a different format** by running:
  ```bash
  yt-dlp -g "URL_HERE"
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

## 🎯 Summary
✅ **Install Python & dependencies**  
✅ **Find and use a working video stream URL**  
✅ **Run the detection script**  
✅ **Analyze detected vehicles in real time**  

---

💡 **Developed using Python, OpenCV, and YOLOv8.**
