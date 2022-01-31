# -*- coding: utf-8 -*-

from pymetamap import MetaMap
mm = MetaMap.get_instance('/home/arif/Desktop/metamap/public_mm/bin/metamap16')

def metamapExtract(sentenceList):
    conceptNumList=[]
    UMLSconceptList = []
    
    for i in range(len(sentenceList)):
        conceptNumList.append(i+1)
        
    concepts,error = mm.extract_concepts(sentenceList, conceptNumList)
    
    for concept in concepts:
        #print(concept)
        #print("******************")
        if (float(concept[2])>9.99):
            UMLSconceptList.append(concept)
            
# =============================================================================
#     for conceptGT10 in UMLSconceptList:
#         print(conceptGT10[2])
#         print(conceptGT10[6][-2])
#         print("##########")
# =============================================================================
    return UMLSconceptList