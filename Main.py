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

                

            # Display the frame
            cv2.imshow('Tracking Frame', frame)

            if cv2.waitKey(1) & 0xFF == 27: # Press 'Esc' to exit
                break
    

    cap.release()
    cv2.destroyAllWindows()


main()