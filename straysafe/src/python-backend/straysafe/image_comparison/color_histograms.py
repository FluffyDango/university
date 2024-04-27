import cv2
from . import img1, img2

def calc_histograms():
    hist_img1 = cv2.calcHist([img1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_img2 = cv2.calcHist([img2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    metric_val = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_BHATTACHARYYA)
    print(metric_val)


def calc_histograms_and_visualize():
    import matplotlib.pyplot as plt

    color = ('b', 'g', 'r')
    plt.figure(figsize=(16, 6))

    for i, col in enumerate(color):
        hist_img1 = cv2.calcHist([img1], [i], None, [256], [0, 256])
        cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        plt.subplot(2, 3, i + 1)
        plt.plot(hist_img1, color=col)
        plt.title(f'Hist for {col.upper()} in Image 1')

        hist_img2 = cv2.calcHist([img2], [i], None, [256], [0, 256])
        cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        plt.subplot(2, 3, i + 4)
        plt.plot(hist_img2, color=col)
        plt.title(f'Hist for {col.upper()} in Image 2')


    metric_val = []
    for i in range(3):
        hist1 = cv2.calcHist([img1], [i], None, [256], [0, 256])
        hist2 = cv2.calcHist([img2], [i], None, [256], [0, 256])
        cv2.normalize(hist1, hist1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        cv2.normalize(hist2, hist2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
        metric_val.append(cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA))
    
    plt.show()
    print("Comparison Metrics (Blue, Green, Red):", metric_val)