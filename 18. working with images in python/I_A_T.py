import cv2

image = cv2.imread("sunset.png")

def draw_cilcle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 20, (0, 255, 0), -1)
        cv2.imshow("Image Annotation tool", image)

cv2.imshow("Image Annotation Tool", image)
cv2.setMouseCallback("Image Annotation Tool", draw_cilcle)

cv2.waitKey(0)
cv2.destroyAllWindows()