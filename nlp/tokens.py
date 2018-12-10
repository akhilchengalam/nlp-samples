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


tokens = [t for t in text.split()] 
freq = nltk.FreqDist(tokens) 
clean_tokens = tokens[:] 
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

#find count of frequently used tokens and write it to a file
freq = nltk.FreqDist(clean_tokens)
f= open("files/"+file_name+"_tokenization.txt","w+")
f.write("**************************Tokens**************************\n\n")
f.write(str(freq.items()))
f.close()
#plot a gaph that shows the count of frequently used tokens
freq.plot(30,cumulative=False)

#remove the images created for extraction
for im in pngnames:
    os.remove(im)

