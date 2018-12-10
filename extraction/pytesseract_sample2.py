try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from wand.image import Image
import cv2

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

file_name = 'attachments/DOC-1.pdf'
with Image(filename=file_name, resolution=300) as Sourcefilename:
    
	images=Sourcefilename.sequence
	pages=len(images) # no of pages in PDF
	pngnames=[]
	pdfpath = file_name
	pdffilename = file_name
	for i in range(pages):
	   Image(images[i]).save(filename= pdfpath.replace(pdffilename,'') + pdffilename.replace('.pdf','')+ '_page_' + str(i)+'.png') # Save each pages as png
	   pngnames.append(pdfpath.replace(pdffilename,'') + pdffilename.replace('.pdf','')+ '_page_' + str(i)+'.png') # Generate URL for tessaract OCR           
	for p in pngnames:
		print(pytesseract.image_to_string(cv2.imread(p)))
		print("**********************************************************************************************")
		print("**********************************************************************************************")
		print("**********************************************************************************************")



# Simple image to string
# print(pytesseract.image_to_string(Image.open('test.jpg')))

# French text image to string
# print(pytesseract.image_to_string(Image.open('1-european.jpg'), lang='fra'))

# Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('test.jpg')))
# print("***********************************************")
# print("***********************************************")
# print("***********************************************")

# Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('test.jpg')))
# print("***********************************************")
# print("***********************************************")
# print("***********************************************")

# Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('test.jpg')))
# print("***********************************************")
# print("***********************************************")
# print("***********************************************")

# In order to bypass the internal image conversions, just use relative or absolute image path
# NOTE: If you don't use supported images, tesseract will return error
# print(pytesseract.image_to_string('test.jpg'))
# print("***********************************************")
# print("***********************************************")
# print("***********************************************")

# get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('test.jpg', extension='pdf')

# get HOCR output
hocr = pytesseract.image_to_pdf_or_hocr('test.jpg', extension='hocr')
