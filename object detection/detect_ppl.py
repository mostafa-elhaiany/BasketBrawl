import torch
import cv2

# Load YOLOv5 nano model (lightweight version)
model = torch.hub.load('ultralytics/yolov5', 'yolov5n')

cap = cv2.VideoCapture(0)
frame_skip = 2
frame_count = 0

left_color = (255, 0, 0)  # Red
right_color = (0, 255, 0)  # Green

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue

    small_frame = cv2.resize(frame, (640, 480))

    img = [small_frame]

    results = model(img)

    bboxes = []
    for *box, conf, cls in results.xyxy[0]:
        if int(cls) == 0:  # Check if the detected class is 'person' (class id 0)
            x1, y1, x2, y2 = map(int, box)
            bboxes.append((x1, y1, x2, y2))

    # Sort bboxes by the x-coordinate
    bboxes.sort(key=lambda x: x[0])

    for i, (x1, y1, x2, y2) in enumerate(bboxes):
        label = f'Person {i + 1}'
        color = left_color if i == 0 else right_color
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow('People Detection', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
