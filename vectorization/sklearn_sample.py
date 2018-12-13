import cv2
import os

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from wand.image import Image
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer


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
	text += pytesseract.image_to_string(cv2.imread(p))

#sklearn CountVectorizer
vectorizer = CountVectorizer(analyzer = "word", tokenizer = None, preprocessor = None, stop_words = None, max_features = 5000) 
train_data_features = vectorizer.fit_transform(sent_tokenize(text))

f = open("files/"+file_name+"-sklearn.txt","w+")

for sentence in sent_tokenize(text):
	vector = vectorizer.transform([sentence]).toarray()
	f.write(str(sentence.encode('utf-8')))
	f.write(str(vector))
	f.write("\n\n\n")
f.close()

for im in pngnames:
    os.remove(im)