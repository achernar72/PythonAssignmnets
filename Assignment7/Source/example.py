import io
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
print("/*************************REading the file in console***************************************/\n\n")
file1 = open("test.txt")
if file1.mode=='r':
 c=file1.read()
 print(c)
line = file1.read()# Use this to read file content as a stream:
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('filteredtext.txt','a')
        appendFile.write(" "+r)
        appendFile.close()
a=open("filteredtext.txt","r")
if a.mode=='r':
 b=a.read()
 print("/................... THis is the  Remove all the words like “a the ! ? ...” Which does not have meaning using stopwords in NLTK...................../\n\n")
 print(b)
 print("\n")
 print("/.................................Using Lemmatization, apply lemmatization on the remaining word................/")
file2=open("test.txt")
if file2.mode=='r':
     e=file2.read()
word=e.split()
print(word)
for r in word:
    number = WordNetLemmatizer().lemmatize(word, 'v')
    print("a")
    print(number)
    if not r in number:
        appendFile = open('filteredtex.txt','a')
        appendFile.write(" "+r)
        appendFile.close()
a=open("filteredtex.txt","r")
if a.mode=='r':
 d=a.read()
print(d)
print("/........... using parts of speech........../")
