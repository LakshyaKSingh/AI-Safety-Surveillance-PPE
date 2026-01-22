from ultralytics import YOLO

class PersonDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def track(self, frame):
        results = self.model.track(
            frame,
            persist=True,
            classes=[0],   # person only
            conf=0.4,
            iou=0.5,
            tracker="bytetrack.yaml"
        )
        return results[0]
