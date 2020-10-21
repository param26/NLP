import numpy as np
import Levenshtein
import nltk
import re
import itertools

t1 = open("text1.txt","r+",errors = 'ignore')
t2 = open("text2.txt","r+",errors = 'ignore')

word1 = t1.read()
word2 = t2.read()

text1 = []
text2 = []

for x in nltk.sent_tokenize(word1):
	text1.append(x)
for x in nltk.sent_tokenize(word2):
	text2.append(x)
# print(len(text1))
cnt = 0
for x1,x2 in list(itertools.product(text1,text2)):
	if Levenshtein.distance(x1,x2) <= len(x1)/2:
		cnt+=1
		print(x1 + " ----- " + x2)
cntx = 0;
print(cnt)
