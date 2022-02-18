import os
import pytesseract

if os.getenv('TESSERACT_PATH'):
    pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_PATH')

text = pytesseract.image_to_string('./image.png', lang='rus')

print(text)