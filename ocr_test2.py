try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
from sys import platform
import cv2
import json

#Configurations
#Load config based on OS
if platform == "linux" or platform == "linux2":
    with open("lin_config.json") as json_data_file:
        data = json.load(json_data_file)
elif platform == "win32":
    with open("win_config.json") as json_data_file:
        data = json.load(json_data_file)

pytesseract.pytesseract.tesseract_cmd = data["tesseract_path"]
image_path = "C:\\projects\\ocr-component\\raw_img\\day_no.png"
current_path = os.getcwd()

def read_image(image_path, threshold):
    tmp_file_path = "C:\\projects\\ocr-component\\raw_img\\temp.png"
    # tmp_file_path.replace('\', "\\")
    originalImage = cv2.imread(image_path)
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, threshold, 255, cv2.THRESH_BINARY)
    cv2.imwrite(tmp_file_path, blackAndWhiteImage)
    print(pytesseract.image_to_string(Image.open("C:\\projects\\ocr-component\\raw_img\\temp.png")))
read_image(image_path, 100)
# # If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
# # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# # Simple image to string
# print(pytesseract.image_to_string(Image.open('test.png')))
