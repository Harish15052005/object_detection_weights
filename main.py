from ultralytics import YOLO
import cv2

# model = YOLO('yolov8n.pt')
model = YOLO('best.pt')
results = model("img1.jpeg", save=True)
