import numpy as np
import re
import nltk 
import cv2
import os
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from wand.image import Image

#Bag of Words model
def bagofwords(sentence, words):
    sentence_words = word_tokenize(sentence)
    # frequency word count
    bag = np.zeros(len(words))
    for sw in sentence_words:
        for i,word in enumerate(words):
            if str(word) == str(sw):
                bag[i] += 1
                
    return np.array(bag)


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

#create a vocabulary
vocabulary = []
for item in freq.items():
	vocabulary.append(item[0])

f = open("files/"+file_name+"bag_of_words.txt","w+")

for sentence in sent_tokenize(text.decode('utf-8')):
	vector = bagofwords(sentence.encode('utf-8'), vocabulary)
	f.write(sentence.encode('utf-8'))
	f.write(str(vector))
	f.write("\n\n\n")
f.close()

for im in pngnames:
    os.remove(im)