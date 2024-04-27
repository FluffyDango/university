import cv2
from skimage.metrics import structural_similarity as compare_ssim
import matplotlib.pyplot as plt

from . import img1, img2, target_size


def compute_ssim(img1, img2):
    img1 = cv2.resize(img1, target_size, interpolation=cv2.INTER_LINEAR)
    img2 = cv2.resize(img2, target_size, interpolation=cv2.INTER_LINEAR)

    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calculate SSIM between two grayscale images
    ssim, diff = compare_ssim(gray1, gray2, full=True)
    return ssim, diff

def use_ssim():
    ssim_value, ssim_diff = compute_ssim(img1, img2)
    print(f"SSIM: {ssim_value}")

    plt.figure(figsize=(10, 5))
    plt.imshow(ssim_diff, cmap='coolwarm')
    plt.colorbar()
    plt.title("SSIM Difference Image")
    plt.show()
