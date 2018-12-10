from nltk.stem import WordNetLemmatizer 
from nltk.stem import PorterStemmer 


stemmer = PorterStemmer() 
lemmatizer = WordNetLemmatizer() 
print('****Stemming****')
print(stemmer.stem('stones')) 
print(stemmer.stem('speaking')) 
print(stemmer.stem('bedroom')) 
print(stemmer.stem('jokes')) 
print(stemmer.stem('lisa')) 
print(stemmer.stem('purple')) 
print('============================================')
print('****Lemmetizing****') 
print(lemmatizer.lemmatize('stones')) 
print(lemmatizer.lemmatize('speaking'))
print(lemmatizer.lemmatize('bedroom'))
print(lemmatizer.lemmatize('jokes'))
print(lemmatizer.lemmatize('lisa'))
print(lemmatizer.lemmatize('purple'))
