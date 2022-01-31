# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 01:07:25 2018

@author: Arif
"""

import xlrd
from nltk import sent_tokenize
import os
# =============================================================================
# def replace_with_underscores(cell):
#     return cell.value.replace("","_")
# =============================================================================

wb = xlrd.open_workbook("/home/arif/Desktop/mycode/mycode6/TestData_RAA_FromSile.xlsx")
sh = wb.sheet_by_index(0)

h1='Narratives.\n'
h2='Concepts.\n'
h3='Incorect Concepts.\n'
h4='Additional Concepts.\n'

fileSeq = -1


for row in sh.get_rows():
# =============================================================================
#     artist = replace_with_underscores(row[0])
#     album = replace_with_underscores(row[1])
# =============================================================================
    narratives2 = row[7].value
    narratives3 = narratives2.replace(".",". ")
    narratives = sent_tokenize(narratives3)
    
    #concepts1 = row[1].value
    #concepts2 = concepts1.replace("(","(")
    #concepts3 = concepts2.replace(")","). ")
    #concepts = sent_tokenize(concepts3)   
    
# =============================================================================
#     incorrectConcepts1 = (row[2].value)
#     incorrectConcepts2 = incorrectConcepts1.replace("(","(")
#     incorrectConcepts3 = incorrectConcepts2.replace(")","). ")
#     incorrectConcepts = sent_tokenize(incorrectConcepts3)
#     
#     additionalConcepts1 = (row[3].value)
#     additionalConcepts2 = additionalConcepts1.replace("(","(")
#     additionalConcepts3 = additionalConcepts2.replace(")","). ")
#     additionalConcepts = sent_tokenize(additionalConcepts3)
# =============================================================================
    
# =============================================================================
#     vitals1 = row[4].value
#     vitals2 = vitals1.replace("{","")
#     vitals3 = vitals2.replace("}",". ")
#     vitals = sent_tokenize(vitals3)
#     
#     interventions1 = row[5].value
#     interventions2 = interventions1.replace("{","")
#     interventions3 = interventions2.replace("}",". ")
#     interventions = sent_tokenize(interventions3)
#     
#     narratives1 = row[6].value
#     narratives2 = narratives1.replace("{","")
#     narratives3 = narratives2.replace("}",". ")
#     narratives = sent_tokenize(narratives3)
#     
#     outcome = row[7].value
# =============================================================================

    
    fileSeq=fileSeq+1
    filename = str(fileSeq)+".txt"
    dirname = '/home/arif/Desktop/mycode/mycode6/PaperDummy1'
    os.chdir(dirname)
    with open(filename, 'w') as f:
        #f.write("Report No.\tConcept\tSentence\tNegated or Affirmed\n")
        count=0
        for sents in narratives:
            count=count+1
            sents = sents.encode('ascii', 'ignore').decode('ascii')
            f.write(sents)
            #f.write(str(count)+"\t"+"DUMMY PHRASE"+"\t"+sents+"\t"+"Affirmed"+"\n")
            #f.write("CaseNumber"+str(fileSeq)+"\t"+sents+"\n")
        #f.write(". END.\n\n\n"+h2)
        f.close()
# =============================================================================
#         for sents in concepts:
#             sents = sents.encode('ascii', 'ignore').decode('ascii')
#             f.write(sents+"\n")
#         f.write("\n\n"+h3)
#         for sents in incorrectConcepts:
#             sents = sents.encode('ascii', 'ignore').decode('ascii')
#             f.write(sents+"\n")
#         f.write("\n\n"+h4)
#         for sents in additionalConcepts:
#             sents = sents.encode('ascii', 'ignore').decode('ascii')
#             f.write(sents+"\n")
#         f.write("\n\n")
# =============================================================================

        

# =============================================================================
# fileSeq=fileSeq+1
# filename = "RAAcase"+str(fileSeq)+".txt"
# with open(filename, 'w') as f:
#     f.write(h0+str(int(priority)))
#     f.write(".\n\n")
#     f.write(h1+callType)
#     f.write(".\n\n")
#     f.write(h2+chiefComplaint)
#     f.write("\n\n")
#     for sents in impression:
#         f.write(h3+sents+"\n")
#     f.write("\n")
#     for sents in vitals:
#         f.write(h4+sents+"\n")
#     f.write("\n")
#     for sents in interventions:
#         f.write(h5+sents+"\n")
#     f.write("\n")
#     for sents in narratives:
#         sents = sents.encode('ascii', 'ignore').decode('ascii')
#         f.write(h6+sents+"\n")
#     f.write("\n")
#     f.write(h7+outcome)
#     f.write(".\n")
# =============================================================================

print("Done !")
