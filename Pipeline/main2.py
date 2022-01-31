# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
from Tkinter import *

#import nltk
#from nltk.book import *
#from fpdf import FPDF
from functions import textParse2
from functions import prescription_form2
from functions import gui2

import os
execfile('functions/readText2.py')
#print(output)

sentsList = textParse2.sent_tokenize(output) #final sentences
#print(len(sentsList))
#print(sentsList)
# =============================================================================
# for sents in sentsList:
#     print (sents + '\n')
# =============================================================================

wordsList = textParse2.word_tokenize(output) #final words
#print(len(wordsList))

# =============================================================================
# if 'GCSE' in wordsList:
#     print (wordsList.index('GCSE'))
# =============================================================================

# =============================================================================
# for words in wordsList:
#     print (words + '\n')
# =============================================================================
#print(wordsList[502])

prescription_form2.generateFields(sentsList,wordsList,dummy12)

#print(os.getcwd())

print("!! ______________________________ !!")
