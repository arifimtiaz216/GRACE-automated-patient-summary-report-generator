#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:33:30 2018

@author: arif
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
count = 1
filepath = '/home/arif/Desktop/mycode/mycode6/Paper'




for row in sh.get_rows():
    if(fileSeq == -1):
        fileSeq = fileSeq+1
        continue
# =============================================================================
#     artist = replace_with_underscores(row[0])
#     album = replace_with_underscores(row[1])
# =============================================================================
    narratives2 = row[7].value
    narratives3 = narratives2.replace(".",". ")
    narratives = sent_tokenize(narratives3)
    
    
    fileSeq=fileSeq+1
    filename1 = '/OP'+str(fileSeq)+'.txt'
    fpname = filepath+filename1
    filename = str(fileSeq)+".txt"
    dirname = '/home/arif/Desktop/mycode/mycode6/Paper'
    os.chdir(dirname)
    with open(filename, 'w') as f:
        with open(fpname) as fp:

        #f.write("Report No.\tConcept\tSentence\tNegated or Affirmed\n")
        #count=0
            for sents in narratives:
                line = str(fp.readline())
                rf2=line.rsplit('-', 1)[1]
                rf=rf2.rstrip()
                #print(rf)
                
                line=str(fp.readline())
                line=str(fp.readline())
                #count=count+1
                sents = sents.encode('ascii', 'ignore').decode('ascii')
                #f.write(sents)
                #f.write(str(count)+"\t"+"DUMMY PHRASE"+"\t"+sents+"\t"+"Affirmed"+"\n")
                if(str(rf).startswith("aff")):
                    f.write("CaseNumber"+str(fileSeq)+"\t"+sents+"\n")
                else:
                    f.write("CaseNumber"+str(fileSeq)+"\t"+sents+"\t"+rf+"\n")
            #f.write(". END.\n\n\n"+h2)
            fp.close()
        f.close()
        
with open ("all_results.txt", 'w') as ff:
    for i in range(1,167):
        fln=str(i)+".txt"
        with open(fln, 'r') as ff2:
            all_of_it=ff2.read()
            ff2.close()
        ff.write(all_of_it)
    ff.close()
        
print("Done!")




