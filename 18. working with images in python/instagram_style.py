import cv2
import numpy as np

def instagram_filter(image_path):

    image = cv2.imread(image_path)

    bright_contrast = cv2.convertScaleAbs(image, alpha=1.3, beta=20)


    blurred = cv2.GaussianBlur(bright_contrast, (7, 7), 0)

    warm_image = blurred.copy()
    warm_image[:, :, 2] = cv2.add(warm_image[:, :, 2], 30)
    warm_image[:, :, 1] = cv2.add(warm_image[:, :, 1], 10)

    rows, cols = warm_image.shape[:2]
    kernel_x = cv2.getGaussianKernel(cols, 300)
    kernel_y = cv2.getGaussianKernel(rows, 300)
    kernel = kernel_y * kernel_x.T
    mask = 255 * kernel / np.max(kernel)
    vignette = np.uint8(mask)

    for i in range(3):
        warm_image[:, :, i] = cv2.addWeighted(warm_image[:, :, i], 0.8, vignette, 0.2, 0)



    cv2.imshow("instagram style filter", warm_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


instagram_filter("sunset.png")


