import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model (use 'yolov8m.pt' for better accuracy)
model = YOLO("yolov8m.pt")

# Define the vehicle classes we want to detect
valid_classes = ["car", "bus", "truck", "motorbike"]
excluded_classes = ["boat", "ship", "airplane"]

# Path to the MP4 video file (change this to your video file path)
video_path = "video1.mp4"  # Change this to the correct file path

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if video file opened successfully
if not cap.isOpened():
    print("❌ Error: Could not open video file.")
    exit()

# Create OpenCV display window
cv2.namedWindow("YOLOv8 Vehicle Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("YOLOv8 Vehicle Detection", 1280, 720)  # Resize window for better visibility

while True:
    ret, frame = cap.read()
    if not ret:
        print("🎬 Video ended or cannot read frame.")
        break

    # Convert frame to RGB (YOLO expects RGB, OpenCV loads in BGR)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run YOLOv8 inference with a lower confidence threshold
    results = model(frame_rgb, conf=0.03, iou=0.5)

    # Draw bounding boxes for detected vehicles
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            confidence = float(box.conf[0])  # Confidence score
            class_id = int(box.cls[0])  # Class ID
            label = model.names[class_id]  # Class name

            # Print detected labels for debugging
            print(f"🔍 Detected: {label} ({confidence:.2f})")

            # Ignore boats & non-vehicle objects
            if label in excluded_classes:
                print(f"⚠️ Skipping {label} (not a vehicle)")
                continue

            # Only detect valid vehicle classes
            if label in valid_classes:
                color = (0, 255, 0)  # Green bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Show the frame with detections
    cv2.imshow("YOLOv8 Vehicle Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
