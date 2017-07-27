import io
#from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#word_tokenize accepts a string as an input, not a file.
#stop_words = set(stopwords.words('a'))
file=open("test.txt","r");
if file.mode=='r':
 a=file.read()
 print(a)

