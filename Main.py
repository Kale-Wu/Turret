import cv2
import mediapipe as mp
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break
        
            # Flip the frame horizontally
            frame = cv2.flip(frame, 1)  
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb_frame)

            if results.pose_landmarks:
                # Draw landmarks on the frame
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            print("Nose coordinates:", get_Nose_coordinates(results.pose_landmarks, frame.shape[1], frame.shape[0]))

            # Display the frame
            cv2.imshow('Tracking Frame', frame)

            if cv2.waitKey(1) & 0xFF == 27: # Press 'Esc' to exit
                break
    
    cap.release()
    cv2.destroyAllWindows()

# All coordinates (0,0) at top-left
def get_landmark_coordinates(landmarks, width, height):
    coordinates = []
    for landmark in landmarks.landmark:
        x = int(landmark.x * width)
        y = int(landmark.y * height)
        coordinates.append((x, y))
    return coordinates

# Nose coordinates only
def get_Nose_coordinates(landmarks, width, height):
    if landmarks is None:
        return None
    nose = landmarks.landmark[mp.solutions.pose.PoseLandmark.NOSE]
    x = int(nose.x * width)
    y = int(nose.y * height)
    return (x, y)


main()