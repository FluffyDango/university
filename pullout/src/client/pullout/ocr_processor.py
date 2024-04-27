import pytesseract
import time
from pullout import DEBUG

def scan_text(image):
    e1 = time.time()
    # Use Tesseract to do OCR on the image
    config = "-c tessedit_char_whitelist='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZąčęėįšųūĄČĘĖĮŠŲŪ@-+.,/\" ' --psm 6 --oem 1"
    text = pytesseract.image_to_string(image, lang='lit', config=config)
    e2 = time.time()
    if DEBUG:
        print("Tesseract took: ", e2 - e1, "seconds")

    return text