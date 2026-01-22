import cv2
from detector import PersonDetector
from tracker import SimpleTracker
from violation import ViolationTracker

video_path = "../data/videos/input.mp4"

cap = cv2.VideoCapture(video_path)

detector = PersonDetector()
tracker = SimpleTracker()
violations = ViolationTracker()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    detections = detector.detect(frame)
    tracked_people = tracker.update(detections)

    for track_id, x1, y1, x2, y2 in tracked_people:
        duration = violations.update(track_id, missing_ppe=True)

        color = (0, 0, 255) if duration > 3 else (0, 255, 0)
        cv2.rectangle(frame, (x1,y1), (x2,y2), color, 2)
        cv2.putText(frame, f"ID:{track_id} {int(duration)}s",
                    (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, color, 2)

    cv2.imshow("Safety Surveillance", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
