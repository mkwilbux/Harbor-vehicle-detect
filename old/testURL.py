import cv2
import requests
import numpy as np

url = "https://ie.trafficland.com/v2.0/8378/huge?system=weatherbug-cmn&pubtoken=7c40c33aadf00c0a20e9de7e8485913445d83bd8b0b87c176f6c656f93c46464&refreshRate=2000&rnd=1741899863718"

while True:
    try:
        # Fetch image from URL
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
            frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

            if frame is not None:
                cv2.imshow('Live Stream', frame)

        # Refresh every 2 seconds (as per `refreshRate=2000`)
        if cv2.waitKey(2000) & 0xFF == ord('q'):
            break

    except Exception as e:
        print(f"Error: {e}")
        break

cv2.destroyAllWindows()
