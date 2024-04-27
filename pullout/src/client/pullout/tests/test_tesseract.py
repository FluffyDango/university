import sys
import unittest
import cv2
sys.path.append('../')
from pullout.tesseract.img_preprocessing import ImagePreprocesor
from pullout import base_path
import os

class TestTesseract(unittest.TestCase):
    def setUp(self):
        self.processor = ImagePreprocesor()
        self.image_path = os.path.join(base_path, 'tests', 'testImage.JPG')
        self.image = cv2.imread(self.image_path, cv2.IMREAD_COLOR)

    def test_grayscale_conversion(self):
        grayscale_result = self.processor.edge_detection(self.image)

        self.assertEqual(len(grayscale_result.shape), 2)
        self.assertEqual(grayscale_result.shape[2], 1)
        
    def test_image_resizer(self):
        resized_result = self.processor.image_resizer(self.image)

        self.assertEqual(resized_result.shape[1], 500)

    def test_dilate_image(self):
        dilated_result = self.processor.dilate_image(self.image)
    
        self.assertTrue((dilated_result > self.image).any())