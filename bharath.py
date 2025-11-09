import cv2
import numpy as np
import os

def cartoonize_frame(frame):
    """Convert a single video frame to cartoon style."""
    # 1. Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)

    # 2. Edge detection
    edges = cv2.adaptiveThreshold(gray, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # 3. Smooth color image
    color = cv2.bilateralFilter(frame, 9, 300, 300)

    # 4. Combine edges + color
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    ret
