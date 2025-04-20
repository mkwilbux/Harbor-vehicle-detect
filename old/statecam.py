# GPLv3
# march 2025
# mwilbux: Marcia Wilbur
# gnu at asu dot edu
import cv2
import requests
import numpy as np
import torch
from ultralytics import YOLO

# Load YOLOv11 model (automatically downloads if not found)
model = YOLO("yolov8n.pt")  # Use "yolov8s.pt" or "yolov8m.pt" for better accuracy

# Traffic camera image URL
url = "https://ie.trafficland.com/v2.0/8378/huge?system=weatherbug-cmn&pubtoken=7c40c33aadf00c0a20e9de7e8485913445d83bd8b0b87c176f6c656f93c46464&refreshRate=2000"

while True:
    try:
        # Fetch the latest image from the URL
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
            frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            if frame is None:
                continue  # Skip if the image is invalid

            # Run YOLOv11 detection on the frame
            results = model(frame)

            # Draw bounding boxes
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get box coordinates
                    conf = box.conf[0].item()  # Confidence score
                    cls = int(box.cls[0].item())  # Class ID
                    label = model.names[cls]  # Class name

                    # Only detect people and vehicles
                    if label in ["person", "car", "bus", "truck", "motorcycle"]:
                        color = (0, 255, 0) if label == "person" else (0, 0, 255)  # Green for people, Red for vehicles
                        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Show the output frame
            cv2.imshow("Norwich, CT 395 exit 13", frame)

        # Refresh every 2 seconds (matches the camera update rate)
        if cv2.waitKey(2000) & 0xFF == ord('q'):
            break

    except Exception as e:
        print(f"Error: {e}")
        break

cv2.destroyAllWindows()
