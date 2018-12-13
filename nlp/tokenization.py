import nltk 
import cv2
import os
from nltk.corpus import stopwords

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from wand.image import Image
from nltk.tokenize import sent_tokenize, word_tokenize


#Extract text from a pdf file and tokenize the words present.
#Find count of frequently used tokens

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

text = ''
for p in pngnames:
	text += pytesseract.image_to_string(cv2.imread(p)).encode('utf-8')

f= open("files/"+file_name+"_word_tokens.txt","w+")
f.write("**************************Word Tokens**************************\n\n")
f.write(str(word_tokenize(text.decode('utf-8'))))
f.close()

f= open("files/"+file_name+"_sentence_tokens.txt","w+")
f.write("**************************Sentence Tokens**************************\n\n")
f.write(str(sent_tokenize(text.decode('utf-8'))))
f.close()

#remove the images created for extraction
for im in pngnames:
    os.remove(im)

