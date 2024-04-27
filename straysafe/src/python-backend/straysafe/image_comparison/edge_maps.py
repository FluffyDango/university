from . import img1, img2, target_size
import cv2
from matplotlib import pyplot as plt
import numpy as np

def compute_edges(image, low_threshold=50, high_threshold=150):
    resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
    # Convert the image to grayscale
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian Blur to smooth the image and reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Apply Canny edge detection
    edges = cv2.Canny(blurred, low_threshold, high_threshold)
    return edges

def calc_edge_maps():
    edges_img1 = compute_edges(img1)
    edges_img2 = compute_edges(img2)

    # Compute absolute difference between the edge images
    diff = cv2.absdiff(edges_img1, edges_img2)
    # Count non-zero pixels in the difference image
    non_zero_count = np.count_nonzero(diff)
    # Normalize the count by the total number of pixels to get a dissimilarity measure
    total_pixels = diff.size
    dissimilarity = non_zero_count / total_pixels
    similarity = 1 - dissimilarity

    print(f"Similarity Score: {similarity}")

    plt.figure(figsize=(15, 5))
    plt.subplot(131), plt.imshow(edges_img1, cmap='gray'), plt.title('Edges of Image 1')
    plt.subplot(132), plt.imshow(edges_img2, cmap='gray'), plt.title('Edges of Image 2')
    plt.subplot(133), plt.imshow(diff, cmap='gray'), plt.title('Difference of Edges')
    plt.show()