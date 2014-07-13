# -*- coding: utf-8 -*- 
import nltk
import csv
import time

dicdata = {}
f = open('output.csv', 'rb')

dataReader = csv.reader(f)

for row in dataReader:
	dicdata.update({unicode(row[1]):unicode(row[2])})
   
#print dicdata["reforming"]
#dic.has_key('age')

#time.sleep(100)
raw = open('text.txt').read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
#print tokens
tokens = [w.lower() for w in tokens]
#print tokens.count("flight")

#stopwords = nltk.corpus.stopwords.words('english')
symbols = ["'", '"', '`', '.', ',', '-', '!', '?', ':', ';', '(', ')']
for symbol in symbols:
	while symbol in tokens:
		tokens.remove(symbol)

#print tokens

taged = nltk.pos_tag(tokens)
words2translate = [x[0] for x in taged if x[1] == "NN"]
#translated = [x for w in words_to_tlanslate if dic.has_key(w) == True x = dicdata[w] else: x = "404"]
translated =[]
print words2translate
for w in words2translate:
	if dicdata.has_key(unicode(w)) == True:
		x = dicdata[unicode(w)]
	else:
		x = u"404"
	translated.append([w,unicode(x)])
	
f = open('translated.csv', 'ab')
csvWriter = csv.writer(f)
for w in translated:
	csvWriter.writerow(w)
	
