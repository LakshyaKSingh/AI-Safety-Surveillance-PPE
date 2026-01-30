import cv2
from detector import PersonDetector
from violation import ViolationTracker

video_path = "E:/Codes/Ignite/data/videos/input.mp4"

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("ERROR: Video not opened")
    exit()

detector = PersonDetector()
violations = ViolationTracker()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = detector.track(frame)

    if results.boxes.id is not None:
        boxes = results.boxes.xyxy.cpu().numpy()
        ids = results.boxes.id.cpu().numpy()

        for box, track_id in zip(boxes, ids):
            x1, y1, x2, y2 = map(int, box)

            # simulate missing PPE for now
            duration = violations.update(int(track_id), missing_ppe=True)

            color = (0, 0, 255) if duration > 3 else (0, 255, 0)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(
                frame,
                f"ID {int(track_id)} | {int(duration)}s",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

    cv2.imshow("Safety Surveillance - Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
