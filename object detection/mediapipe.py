import torch
import cv2
import mediapipe as mp
import time
import random

model = torch.hub.load('ultralytics/yolov5', 'yolov5n')

class PoseDetector():
    def __init__(self, detectionCon=0.5, trackCon=0.5):
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(min_detection_confidence=self.detectionCon,
                                     min_tracking_confidence=self.trackCon)
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    def findPoses(self, img, bboxes, draw=True):
        all_landmarks = []
        color_index = 0
        for bbox in bboxes:
            x, y, w, h = bbox
            if w <= 0 or h <= 0:  # Check for invalid bounding box dimensions
                continue

            person_img = img[y:y + h, x:x + w]
            if person_img.size == 0:  # Check for empty image
                continue

            imgRGB = cv2.cvtColor(person_img, cv2.COLOR_BGR2RGB)
            self.results = self.pose.process(imgRGB)

            if self.results.pose_landmarks:
                landmarks = []
                for landmark in self.results.pose_landmarks.landmark:
                    ih, iw, _ = person_img.shape
                    cx, cy = int(landmark.x * iw) + x, int(landmark.y * ih) + y
                    landmarks.append((cx, cy))
                all_landmarks.append(landmarks)

                if draw:
                    color = self.colors[color_index % len(self.colors)]
                    color_index += 1
                    self.draw_landmarks(img, landmarks, color)

        return img, all_landmarks

    def draw_landmarks(self, img, landmarks, color):
        # Draw connections
        for connection in self.mpPose.POSE_CONNECTIONS:
            start_idx, end_idx = connection
            cv2.line(img, landmarks[start_idx], landmarks[end_idx], color, 2)

        # Draw landmarks
        for landmark in landmarks:
            cv2.circle(img, landmark, 5, color, cv2.FILLED)

def main():
    cap = cv2.VideoCapture(0)
    frame_skip = 2
    frame_count = 0
    detector = PoseDetector()

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
                bboxes.append((x1, y1, x2 - x1, y2 - y1))  # Convert to (x, y, w, h) format

        img, all_landmarks = detector.findPoses(frame, bboxes)

        if all_landmarks:
            print(all_landmarks)

        cv2.imshow('People Detection', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
