import cv2
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

img = cv2.imread(r'test.png')
print(pytesseract.image_to_string(img))
# OR explicit beforehand converting
print("*************************************")
print("*************************************")
print("*************************************")
print(pytesseract.image_to_string(Image.fromarray(img))) 