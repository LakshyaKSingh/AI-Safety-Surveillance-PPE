class SimpleTracker:
    def __init__(self):
        self.next_id = 0
        self.tracks = {}

    def update(self, detections):
        tracked = []
        for box in detections.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            track_id = self.next_id
            self.tracks[track_id] = (x1, y1, x2, y2)
            tracked.append((track_id, x1, y1, x2, y2))
            self.next_id += 1
        return tracked
