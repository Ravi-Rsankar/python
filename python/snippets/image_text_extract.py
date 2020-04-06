import cv2
import pytesseract

# This is the default location of tesseract when installed in windows
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/name/AppData/Local/Tesseract-OCR/tesseract.exe'

img = cv2.imread('download.png')
text = pytesseract.image_to_string(img)
print(text)

with open('log.txt', 'w') as f:
	f.write(text)

import pandas as pd

df = pd.read_fwf('log.txt')
df.to_csv('log.csv')
