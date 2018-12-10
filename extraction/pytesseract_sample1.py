try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from wand.image import Image
import cv2


file_name = 'policy1.pdf'
with Image(filename=file_name, resolution=300) as Sourcefilename:
    
	images=Sourcefilename.sequence
	pages=len(images) # no of pages in PDF
	pngnames=[]
	pdfpath = file_name
	pdffilename = file_name
	for i in range(pages):
	   Image(images[i]).save(filename= pdfpath.replace(pdffilename,'') + pdffilename.replace('.pdf','')+ '_page_' + str(i)+'.png') # Save each pages as png
	   pngnames.append(pdfpath.replace(pdffilename,'') + pdffilename.replace('.pdf','')+ '_page_' + str(i)+'.png') # Generate URL for tessaract OCR           
	f= open("files/"+file_name+".txt","w+")
	for p in pngnames:
		f.write(pytesseract.image_to_string(cv2.imread(p)).encode('utf-8'))
	f.close()
for im in pngnames:
    os.remove(im)