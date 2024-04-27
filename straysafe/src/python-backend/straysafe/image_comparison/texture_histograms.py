from . import img1, img2
import cv2
import numpy as np

def lbp_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Initialize the LBP image
    lbp = np.zeros_like(gray)
    # Consider each pixel in the image (excluding the borders)
    for i in range(1, gray.shape[0] - 1):
        for j in range(1, gray.shape[1] - 1):
            # Get the center pixel
            center = gray[i, j]
            # Binary pattern
            binary = ''
            binary += '1' if gray[i-1, j-1] > center else '0'
            binary += '1' if gray[i-1, j  ] > center else '0'
            binary += '1' if gray[i-1, j+1] > center else '0'
            binary += '1' if gray[i  , j+1] > center else '0'
            binary += '1' if gray[i+1, j+1] > center else '0'
            binary += '1' if gray[i+1, j  ] > center else '0'
            binary += '1' if gray[i+1, j-1] > center else '0'
            binary += '1' if gray[i  , j-1] > center else '0'
            # Convert binary string to decimal
            lbp[i, j] = int(binary, 2)
    return lbp

def calc_texture_histograms():
    from matplotlib import pyplot as plt
    lbp_img1 = lbp_image(img1)
    lbp_img2 = lbp_image(img2)

    # Compute histograms of LBP images
    hist_img1 = cv2.calcHist([lbp_img1], [0], None, [256], [0, 256])
    hist_img2 = cv2.calcHist([lbp_img2], [0], None, [256], [0, 256])

    # Normalize the histograms
    cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    comparison = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CHISQR)
    print(f"Chi-Squared Distance: {comparison}")

    plt.figure(figsize=(10, 5))
    plt.subplot(121), plt.imshow(lbp_img1, cmap='gray'), plt.title('LBP of Image 1')
    plt.subplot(122), plt.imshow(lbp_img2, cmap='gray'), plt.title('LBP of Image 2')

    plt.figure()
    plt.plot(hist_img1, label='Image 1')
    plt.plot(hist_img2, label='Image 2')
    plt.xlabel('LBP Pattern')
    plt.ylabel('Frequency')
    plt.title('Texture Histograms')
    plt.legend()

    plt.show()