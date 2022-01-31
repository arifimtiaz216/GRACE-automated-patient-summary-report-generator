#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:15:47 2019

@author: arif
"""
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
tokenized_sentences=[]
tokenized_words=[]

sampleUnpunctuatedText="dispatch Priority One for breathing difficulties arrive on scene to find a patient being ambulated out to the residents with Richmond by the Richmond fire department patient complains of shortness of breath and a slightly productive cough since yesterday the etiology of which patient reports that the day prior while minding his own business in a store he was sprayed in the face with some sort of cleaning agent on assessment patient is alert and oriented he's in good color and does not appear to be in extremis he has clear lung sounds and a patent Airway he's takes a number of medications including albuterol aspirin 81 mg daily amlodipine Alprazolam Lasix pantoprazole and Neurontin allergic to Percocet and says he cannot be anywhere near it on contact patient  neither has any traumatic injury loss of consciousness chest pain abdominal pain nausea vomiting diarrhea vertigo syncope current or recent illness suicidal ideation or homicidal ideation recent etoh or drug use his Airway is patent his breathing is adequate circulation is plus two at the is plus 2 at the radial artery patient appeared without distress alert and oriented times 4 and ambulatory with a walker we've got a Walker body survey skin is normal warm and dry skin turgor normal and appropriate color for patient his vital signs are as follows he has a heart rate of 91 resting heart rate of 16 blood pressure of 137 over 73 glucose glucose of 136 GCS of 15 pulse ox at 99% on room air his EKG of sinus rhythm without ectopy or stemi have an IV established 12-lead done and that's it"
print("=============================================================")
print("Unpunctuated Text: ")
print(sampleUnpunctuatedText)
print("=============================================================")

#PRE_PROCESSING
preProcess1=sampleUnpunctuatedText.replace(' ','%20')
preProcess2=preProcess1.replace('\'','%27')
preProcess3=preProcess2.replace('&','%26')
print("=============================================================")
print("Preprocessed Text: ")
print(preProcess3)
print("=============================================================")

addPunctuation1='curl -d text='+preProcess3+' http://bark.phon.ioc.ee/punctuator'
print("=============================================================")
print("First phase punctuation: ")
print(addPunctuation1)
print("=============================================================")

import commands

addPunctuation2 = commands.getstatusoutput(addPunctuation1)
print("=============================================================")
print("Second phase punctuation: ")
print(addPunctuation2)
print("=============================================================")


addPunctuation3 = addPunctuation2[1].rsplit('\n', 1)[1]
print("=============================================================")
print("Final phase punctuation: ")
print(addPunctuation3)
print("=============================================================")


#POST_PROCESSING
addPunctuation3 = addPunctuation3.replace('%20',' ')
addPunctuation3 = addPunctuation3.replace('%27','\'')
addPunctuation3 = addPunctuation3.replace('%26','&')

tokenized_sentences=sent_tokenize(addPunctuation3)
tokenized_words=word_tokenize(addPunctuation3)

print("=============================================================")
print("Tokenized Sentences: ")
for i in range(len(tokenized_sentences)):
    print(str(i+1)+":-->  "+str(tokenized_sentences[i]))
print("=============================================================")

print("=============================================================")
print("Tokenized Words: ")
print(tokenized_words)
print("=============================================================")


from functions import prescription_form2
prescription_form2.generateFields(tokenized_sentences,tokenized_words,sampleUnpunctuatedText)
print("---------------DONE!!----------------")