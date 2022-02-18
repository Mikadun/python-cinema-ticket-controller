import os
import pytesseract

if os.getenv('TESSERACT_PATH'):
    pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_PATH')

print(pytesseract.image_to_string('./image.png', lang='rus'))
print(pytesseract.image_to_string('./image2.png', lang='rus'))
