import cv2
import numpy as np
from ultralytics import YOLO

# Load the YOLOv8 model (Use 'yolov8m.pt' or 'yolov8x.pt' for better accuracy)
model = YOLO("yolov8m.pt")

# Define the vehicle classes to detect
valid_classes = ["car", "bus", "truck", "motorbike"]
excluded_classes = ["boat", "ship", "airplane"]

# Open the webcam (0 = default camera, 1 = external camera)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("❌ Error: Could not open webcam.")
    exit()

# Create an OpenCV display window
cv2.namedWindow("YOLOv8 Vehicle Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("YOLOv8 Vehicle Detection", 1280, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Could not read frame from webcam.")
        break

    # Convert frame to RGB (YOLO expects RGB, OpenCV loads in BGR)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run YOLOv8 inference with a low confidence threshold for better detection
    results = model(frame_rgb, conf=0.2, iou=0.5)

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
