import time
import cv2
import numpy as np
from ultralytics import YOLO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ————— CONFIG —————
URL            = "https://civplus.tikiliveapi.com/embed?scheme=embedChannel&channelId=2016&autoplay=yes&showChat=yes"
MODEL_PATH     = "yolov8m.pt"           # or yolov8n.pt / yolov8x.pt
VALID_CLASSES    = {"car","bus","truck","motorbike"}
EXCLUDED_CLASSES = {"boat","ship","airplane"}
FPS               = 10                  # detection frames per second

# ————— LOAD YOLO —————
model = YOLO(MODEL_PATH)

# ————— SELENIUM SETUP —————
opts = Options()
opts.add_argument("--headless")          # comment out to watch the browser
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-gpu")
opts.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=opts)

try:
    # 1) Open the embed page
    driver.get(URL)

    # 2) Wait for the video element to appear
    video_el = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "vjs_video_3_html5_api"))
    )

    # 3) Mute & play via JS
    driver.execute_script("""
        let v = document.getElementById('vjs_video_3_html5_api');
        if(v){
          v.muted = true;
          v.play();
        }
    """)

    # 4) Prepare OpenCV window
    win = "Live Vehicle Detection"
    cv2.namedWindow(win, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(win, 1280, 720)
    delay = int(1000 / FPS)

    # 5) Capture‑and‑detect loop
    while True:
        # screenshot only the <video> element
        png = video_el.screenshot_as_png
        img = cv2.imdecode(np.frombuffer(png, np.uint8), cv2.IMREAD_COLOR)
        if img is None:
            time.sleep(0.1)
            continue

        # YOLO expects RGB
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = model(rgb, conf=0.25, iou=0.5)

        # draw boxes
        for res in results:
            for box in res.boxes:
                cls = int(box.cls[0])
                label = res.names[cls]
                if label in EXCLUDED_CLASSES:
                    continue
                if label in VALID_CLASSES:
                    x1,y1,x2,y2 = map(int, box.xyxy[0])
                    conf = float(box.conf[0])
                    cv2.rectangle(img, (x1,y1),(x2,y2),(0,255,0),2)
                    cv2.putText(img, f"{label} {conf:.2f}", (x1,y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),2)

        cv2.imshow(win, img)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

finally:
    driver.quit()
    cv2.destroyAllWindows()
