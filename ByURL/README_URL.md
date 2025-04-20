# 🚗 Live Vehicle Detection from Embedded Stream

This script uses YOLOv8 and Selenium to detect vehicles (cars, buses, trucks, motorbikes) from a live embedded webcam stream via a headless browser. Results are displayed live in an OpenCV window with bounding boxes.

---

## 📦 Requirements

- Python 3.8+
- Google Chrome (installed)
- ChromeDriver (matching your Chrome version)
- YOLOv8 model file (`yolov8m.pt`) from Ultralytics

### Install Python dependencies

```bash
pip install opencv-python numpy ultralytics selenium
```

---

## 🔧 Setup

1. **Download YOLOv8 Model**

   ```bash
   wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m.pt
   ```

2. **Install ChromeDriver**

   Make sure ChromeDriver matches your Chrome browser version.

   - To check:
     ```bash
     chromedriver --version
     ```

   - On Debian/Ubuntu:
     ```bash
     sudo apt install chromium-chromedriver
     ```

---

## ▶️ Run the Script

```bash
python detect_stream.py
```

> Replace `detect_stream.py` with your actual script filename.

The script will:

- Launch a headless browser
- Open the stream from the embedded video
- Capture live screenshots
- Use YOLOv8 to detect vehicles in real time
- Display the result via OpenCV

---

## 📺 Stream Source

Currently configured to use:

```
https://civplus.tikiliveapi.com/embed?scheme=embedChannel&channelId=2016&autoplay=yes&showChat=yes
```

Change the `URL` in the script to switch to a different video source.

---

## ⚙️ Configurable Options

| Variable | Description |
|----------|-------------|
| `MODEL_PATH` | Path to your YOLOv8 model |
| `VALID_CLASSES` | Set of vehicle types to detect |
| `EXCLUDED_CLASSES` | Objects to ignore |
| `FPS` | Frame capture rate for detection |

---

## 🛑 Exiting

Press **`q`** in the OpenCV display window to quit the script and close the browser cleanly.

---

## 💡 Notes

- No need for `.m3u8` or `.mp4` direct video links. This script works with JavaScript-based embedded streams.
- Can be extended to:
  - Record clips
  - Stream annotated video via Flask
  - Broadcast to platforms like YouTube using FFmpeg

---

## 🧩 Troubleshooting

- If the video fails to load, try removing `--headless` in the script to watch the browser behavior.
- Ensure ChromeDriver is compatible with your Chrome browser version.
