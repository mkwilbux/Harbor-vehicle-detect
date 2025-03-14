# 🚀 Vehicle Recognition Using YOLOv8 (MP4 Video)

This project detects vehicles in an **MP4 video** using **YOLOv8 and OpenCV**.

## 📌 Installation Guide

### **Step 1: Install Python (If Not Installed)**
Ensure you have **Python 3.8+** installed. Check your Python version:

```bash
python3 --version
```

If you don’t have it, [download Python](https://www.python.org/downloads/) and install it.

### **Step 2: Set Up a Virtual Environment (Recommended)**
Using a virtual environment helps keep dependencies clean.

#### 🔹 **Linux/Mac**
```bash
python3 -m venv yolo_env
source yolo_env/bin/activate
```

#### 🔹 **Windows**
```bash
python -m venv yolo_env
yolo_env\Scripts\activate
```

Your terminal should now show `(yolo_env)` before the command prompt.

### **Step 3: Install Required Dependencies**
Run the following command to install OpenCV, YOLO, and other necessary libraries:

```bash
pip install ultralytics opencv-python numpy
```

### **Step 4: Prepare an MP4 Video**
- Place your MP4 video in the same directory as the script.
- Rename it to **`video.mp4`** or update the script with your file’s name.

## 📌 Running the Script

1. **Save the Python script** as `vehicle_recognition_mp4.py`.
2. **Run the script**:
   ```bash
   python3 vehicle_recognition_mp4.py
   ```
3. **Press 'q' to exit** the detection window.

## 📌 Troubleshooting

### ❌ **Issue: "Could not open video file."**
- Ensure **`video.mp4`** exists in the same directory.
- If using another file, update `video_path = "your_video.mp4"` in the script.

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
✅ **Set up a virtual environment**  
✅ **Download or prepare an MP4 video**  
✅ **Run the detection script**  
✅ **Analyze the detected vehicles in real time**  

### ⏭ Next Steps
1️⃣ **Test detection on your video**  
2️⃣ If detection **isn’t accurate**, I can help **fine-tune YOLO for better results**.  
3️⃣ Want to **train a custom model** on specific vehicles? Let me know! 🚀  

---

💡 **Developed using Python, OpenCV, and YOLOv8.**
