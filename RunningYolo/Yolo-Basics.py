from ultralytics import YOLO
import cv2

model = YOLO('../YOLO-weights/yolov8l.pt')
results = model("Images/4.jpg", show=True)
cv2.waitKey(0)