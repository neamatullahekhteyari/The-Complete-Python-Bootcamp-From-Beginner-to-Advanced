import cv2

image = cv2.imread("sunset.png")

cv2.imshow("displayed image", image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("grayscale image", gray_image)
cv2.imshow("HSV image", hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()



annotated_image = image.copy()


# (x1, y1) to (x2, y2)

cv2.rectangle(annotated_image, (50, 50),(250, 200), (0, 255, 0), 3)


cv2.circle(annotated_image, (300, 150), 50, (255, 0, 0), -1 )

cv2.line(annotated_image, (100, 300), (400, 300), (0, 0, 255), 5)


cv2.putText(annotated_image, "OpenCV Drawing", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 255, 255), 2)


cv2.imshow("Annotated image", annotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()