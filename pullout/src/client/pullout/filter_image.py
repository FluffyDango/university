import cv2
import numpy as np
from imutils.perspective import four_point_transform
from pullout import base_path
from pullout import DEBUG
import os
import pytesseract
import time


def open_and_filter_image(image_path: str) -> np.ndarray:
    """Filter image to make it easier for Tesseract to read"""
    kernel = np.ones((5, 5), np.uint8)
    e1 = time.time()
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Detect edges
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    write_debug_image(blurred_image, '1-blurred_image.jpg')
    edge_image = cv2.Canny(blurred_image, 40, 80)
    write_debug_image(edge_image, '2-edge_image.jpg')

    # Dilate the edges so they are thicker
    dilated_image = cv2.morphologyEx(cv2.dilate(edge_image, kernel, iterations = 1), cv2.MORPH_CLOSE, kernel)
    write_debug_image(dilated_image, '3-dilated_image.jpg')

    # Crop out the card
    four_points = find_contours(dilated_image)
    if four_points is None:
        if DEBUG:
            print("\nFilters took: ", time.time() - e1, "seconds")
        return image
    cropped_image = four_point_transform(image, four_points)

    write_debug_image(cropped_image, '5-cropped_image.jpg')

    # It will try to rotate the image if it is not straight but it will fail if the image is too bad
    try:
        angle = pytesseract.image_to_osd(cropped_image, output_type=pytesseract.Output.DICT)['rotate']
        if angle == 90:
            cropped_image = cv2.rotate(cropped_image, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            cropped_image = cv2.rotate(cropped_image, cv2.ROTATE_180)
        elif angle == 270:
            cropped_image = cv2.rotate(cropped_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        
        if angle != 0:
            write_debug_image(cropped_image, '6-rotated_image.jpg')
    except Exception as e:
        pass
    
    if DEBUG:
        print("\nFilters took: ", time.time() - e1, "seconds")

    return cropped_image


def calculate_angle(point1: np.ndarray, center: np.ndarray, point2: np.ndarray):
    vector1 = point1 - center
    vector2 = point2 - center
    dot_product = np.dot(vector1, vector2)
    magnitude_product = np.linalg.norm(vector1) * np.linalg.norm(vector2)
    angle_rad = np.arccos(dot_product / magnitude_product)
    angle_deg = np.degrees(angle_rad)
    return angle_deg

def are_angles_correct(approx) -> bool:
    """Check if the angles of each point are between 80 and 100 degrees"""
    angles = []
    for i in range(len(approx)):
        angle = calculate_angle(
            approx[i - 1][0],
            approx[i][0],
            approx[(i + 1) % len(approx)][0]
        )
        angles.append(angle)
    if 80 < min(angles) < 100 and 80 < max(angles) < 100:
        return True
    else:
        return False

def find_contours(image: np.ndarray) -> np.ndarray:
    """Find the four main points of the card contour"""
    contours, hier = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    four_points = None
    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02*peri, True)
        x, y, w, h = cv2.boundingRect(approx)
        if len(approx) == 4 and are_angles_correct(approx) and w > 100 and h > 100:
            four_points = np.squeeze(approx)
            break
    
    if four_points is None:
        return None
    
    if DEBUG:
        image_copy = image.copy()
        image_copy = cv2.cvtColor(image_copy, cv2.COLOR_GRAY2RGB)
        image_copy = cv2.drawContours(image_copy, [four_points], -1, (0, 255, 0), 3)
        write_debug_image(image_copy, '4-contours.jpg')

    return four_points


def write_debug_image(image: np.ndarray, name: str):
    if DEBUG:
        path = os.path.join(os.getcwd(), 'pullout_debug', name)
        cv2.imwrite(path, image)
