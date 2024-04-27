import os
from straysafe import ASSET_DIR
import cv2

img1 = cv2.imread(os.path.join(ASSET_DIR, 'cat1.jpg'))
img2 = cv2.imread(os.path.join(ASSET_DIR, 'cat2.jpg'))

target_size = (300, 300)