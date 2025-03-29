import cv2
import numpy as np

image = cv2.imread("sunset.png")

alpha = 1.5 
beta = 50 

adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

blurred = cv2.GaussianBlur(image, (15, 15), 0)

# cv2.imshow("blurred image", blurred)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
sharpening_kernel = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                                [-1, -1, -1] ])



sharpened = cv2.filter2D(image, -1, sharpening_kernel)
# cv2.imshow("sharpened image", sharpened)
cv2.imshow("original image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow("brightness and contrast adjusted", adjusted)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Edge detection", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()


