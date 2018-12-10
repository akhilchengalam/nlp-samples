import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from wand.image import Image
import cv2
import os

#classify words to diferent categories

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

document = ''
for p in pngnames:
	document += pytesseract.image_to_string(cv2.imread(p)).encode('utf-8')
sentences = nltk.sent_tokenize(document.decode('utf-8'))   
 
data = []
for sent in sentences:
    data = data + nltk.pos_tag(nltk.word_tokenize(sent))

#filter data based on the type of word and write to a file
f= open("files/"+file_name+"_speech_tagging.txt","w+")
f.write(str(data))
f.close()
#remove the images created for extraction
for im in pngnames:
    os.remove(im)
