import cv2
import mediapipe as mp
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)  

        # Display the frame
        cv2.imshow('Tracking Frame', frame)

        if cv2.waitKey(1) & 0xFF == 27: # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()


main()