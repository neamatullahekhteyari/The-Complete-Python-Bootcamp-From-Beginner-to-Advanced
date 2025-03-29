import cv2
import numpy as np

# Load main image and template
main_image = cv2.imread('scene.jpg')
template = cv2.imread('object.png', 0)

# Convert main image to grayscale
gray_main = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)

# Apply template matching
result = cv2.matchTemplate(gray_main, template, cv2.TM_CCOEFF_NORMED)

# Get the best match location
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Get template size
w, h = template.shape[::-1]

# Draw rectangle around detected object
cv2.rectangle(main_image, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 3)

# Display result
cv2.imshow('Template Matching', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
