# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
from Tkinter import *

#import nltk
#from nltk.book import *
#from fpdf import FPDF
import textParse2
import prescription_form2
#execfile("/home/arif/Desktop/mycode/mycode2/textParse.py")


fileList=[]
wordsList=[] 
sentsList=[] 


myFile=open("file desc2.txt","r")

for eachLine in myFile:
    line=eachLine.strip()
    fileList.append(line)
#print(fileList[1])

myFile.close()

sentences = textParse2.textParsing(fileList)
sentsList = textParse2.sent_tokenize(sentences) #final sentences
#print(sentsList)
wordsList = textParse2.word_tokenize(sentences) #final words
#print(wordsList)
prescription_form2.generateFields(sentsList)

print("!! Summary Created !!")
