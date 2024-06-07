import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create a white canvas to draw on
canvas = None

# Colors for drawing
draw_color = (0, 255, 0)  # Green color
brush_thickness = 5

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for natural interaction
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    results = hands.process(frame_rgb)

    # Initialize canvas if it is None
    if canvas is None:
        canvas = 255 * np.ones_like(frame)

    # Draw hand landmarks if hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the coordinates of the tip of the index finger (landmark 8)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, _ = frame.shape

            x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            # Determine the direction based on finger position
            if y < 100:
                direction = "up"
            elif y > 380:
                direction = "down"
            elif x < 100:
                direction = "left"
            elif x > 540:
                direction = "right"
            else:
                direction = "none"
            
            open('direction.txt', 'w').write(direction)

            # Draw on the canvas
            cv2.circle(canvas, (x, y), brush_thickness, draw_color, -1)

            # Draw the hand landmarks on the frame
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Combine the frame and the canvas
    combined_frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    # Display the combined frame
    cv2.imshow('Hand Paint', combined_frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
