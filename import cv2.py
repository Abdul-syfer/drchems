import cv2
import numpy as np
import os

def cartoonize_frame(frame):
    """Convert a single video frame to cartoon style."""
    # 1. Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)

    # 2. Edge detection
    edges = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 9, 9
    )

    # 3. Smooth color image
    color = cv2.bilateralFilter(frame, 9, 300, 300)

    # 4. Combine edges + color
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon  # ✅ Return the final cartoonized frame


def cartoonize_video(source=0):
    """Capture video from webcam or file and apply cartoon effect."""
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Error: Cannot open video source.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cartoon_frame = cartoonize_frame(frame)

        cv2.imshow("Cartoonized Video", cartoon_frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Run the cartoonizer (0 = webcam)
if __name__ == "__main__":
    cartoonize_video(0)
