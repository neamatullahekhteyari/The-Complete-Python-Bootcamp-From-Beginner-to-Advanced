import cv2
import numpy as np

# Load image
image = cv2.imread('shapes.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours of the shapes
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop through each contour to classify the shape
for contour in contours:
    # Approximate the shape
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
    num_sides = len(approx)
    shape = "Unknown"

    # Define the center of the shape for labeling
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])  # X-coordinate of the center
        cy = int(M["m01"] / M["m00"])  # Y-coordinate of the center
    else:
        cx, cy = 0, 0  # Default values if moment calculation fails

    # Classify shapes based on the number of sides
    if num_sides == 3:
        shape = "Triangle"
        color = (0, 255, 0)  # Green
    elif num_sides == 4:
        # Check if it's a square or rectangle using aspect ratio
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            shape = "Square"
            color = (255, 0, 0)  # Blue
        else:
            shape = "Rectangle"
            color = (0, 255, 255)  # Yellow
    elif num_sides == 5:
        shape = "Pentagon"
        color = (255, 165, 0)  # Orange
    elif num_sides == 6:
        shape = "Hexagon"
        color = (128, 0, 128)  # Purple
    elif num_sides > 8:
        shape = "Circle"
        color = (255, 0, 255)  # Pink

    # Draw the contour of the detected shape
    cv2.drawContours(image, [contour], 0, color, 3)

    # Label the shape name at its center
    cv2.putText(image, shape, (cx - 30, cy),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

# Display the image with detected shapes
cv2.imshow('Shape Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
