try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os

import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
image_path = "C:\\projects\\ocr-component\\raw_img\\level_test.png"
current_path = os.getcwd()

def read_image(image_path, threshold):
    tmp_file_path = os.getcwd() + "\\temp.png"
    originalImage = cv2.imread(image_path)
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, threshold, 255, cv2.THRESH_BINARY)
    cv2.imwrite(tmp_file_path, blackAndWhiteImage)
    print(pytesseract.image_to_string(Image.open(tmp_file_path)))
    return pytesseract.image_to_string(Image.open(tmp_file_path))
read_image(image_path, 70)
# # If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
# # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# # Simple image to string
# print(pytesseract.image_to_string(Image.open('test.png')))
