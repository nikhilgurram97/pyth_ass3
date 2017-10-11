from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist

#reading the file
f=open('file1.txt','r')
fr=str(f.read())

#The Tokenizations
a=sent_tokenize(fr)
b=word_tokenize(fr)
print' The Sentence Tokenizaton:\n'
a1=a[0].split('\n')
print(a1)
print'\n-----\n'
print'The Word Tokenizaton:\n'
print b

#POS and removing verbs
e=pos_tag(b)
e1=[v for v in e if v[1] != 'VBG']
e2=" ".join([v[0] for v in e1])
print'\n-----\n'
print'Parts of Speech1:\n'
print(e1)
print'Parts of Speech2:\n'
print(e2)

#The Lemmatizations
print'\n-----\n'
print'Lemmatization:\n'
l=WordNetLemmatizer()
for k in range(len(b)):
    e1 = l.lemmatize(b[k])
    print ("The word \'" + b[k] + "\' in a Lemmatized Version: " + e1)

#Word Frequency
wd=FreqDist(e2.split(' '))
print'\n-----\n'
print'The Word Frequency:\n'
print(list(wd.most_common(1000)))

#Top5 words
print'\n-----\n'
print'Top 5 words:\n'
top=list(wd.most_common(5))
topd=dict(top)
topw=topd.keys()
print(topw)

