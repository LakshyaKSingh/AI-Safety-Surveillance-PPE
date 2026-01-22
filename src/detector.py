from ultralytics import YOLO

class PersonDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")  # pretrained COCO

    def detect(self, frame):
        results = self.model(frame, classes=[0], conf=0.4)
        return results[0]
