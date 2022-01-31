# -*- coding: utf-8 -*-
import stanfordNER3

from nltk import sent_tokenize

# =============================================================================
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# =============================================================================

import os
import os.path
folder='/home/arif/Desktop/mycode/mycode5/Haydon'

count=0
fileContents=[]
fileSequence=[]

for filename in os.listdir(folder):
    
    count=count+1
    #print(str(count)+"->"+filename)
    
    filepath=os.path.join(folder,filename)
    #print(str(count)+"->"+filepath)
    
    fileSequence.append(filename[:-4])
    #print(fileSequence)
    
    f=open(filepath, 'r')
    fileTextDummy=f.readline()
    fileText=f.readline()
    fileTextStripped=fileText.strip()
    fileContents.append(fileTextStripped)
    #print(fileText)
    f.close()
    
    #fileSequence[i] holds the file number, fileContents[i] holds the content of fileSequence[i].txt  file
    
# =============================================================================
#     print("\n\n\n")
#     print("--------------------------------------------------------------")
#     print("\n\n\n")
# =============================================================================

# =============================================================================
# print("\n")
# print(fileSequence[100])
# print(fileContents[100])    
# print("\n")
# =============================================================================
# =============================================================================
# for i in range(len(fileSequence)):
#     print(fileSequence[i])
#     print(fileContents[i])
#     print(i)
#     print("--------------------------------------------------------------")
# =============================================================================
print("---FILE COUNT: "+str(len(fileContents))+"---\n")
#print("Total count is: "+ str(count)+"\n")

for fileCount in range(len(fileSequence)):
    print("******FILE NUMBER: "+str(fileSequence[fileCount])+"*******")

    #print("***FILE COUNT: "+str(len(fileSequence))+"***")
    sentsList=[]
    #sentsList[i] holds all the sentences of fileContents[i] or fileSequence[i].txt
    #to get the sentences, use sentsList[i][0], sentsList[i][1], sentsList[i][2] etc.
    print("sent_tokenize-started")
    sentsList.append(sent_tokenize(unicode(fileContents[fileCount], errors='ignore')))
    print("sent_tokenize-passed")
    #print(len(sentsList[0]))
    #print(sentsList[0][21])

    
    
    writeDir='/home/arif/Desktop/mycode/mycode5/HaydonN'
    nameOfFile=os.path.join(writeDir, "N"+str(fileSequence[fileCount])+".txt")
    writeFile=open(nameOfFile, "w")
    #print(nameOfFile)
    
    # =============================================================================
    # writeFile=open(nameOfFile, "a")
    # writeFile.write("hiiieeei")
    # writeFile.close()
    # =============================================================================
    print("negDetector-started")   
    for sentenceCount in range(len(sentsList[0])):
        
        treeParsed,posDep=stanfordNER3.negDetector(sentsList[0][sentenceCount])
        
        for i in range(len(posDep)):
            negFlag=0
            #writeFile.write(str(posDep[i]))
            if(posDep[i][1]=='neg'):
                #print(posDep[i])
                print("JackPOT!")
                writeFile.write("\r\nNEG SENTENCE:"+str(sentsList[0][sentenceCount])+"\r\n")
                if(negFlag==0):
                    #writeFile.write(str(treeParsed)+"\r\n\r\n")
                    negFlag=1
                writeFile.write(str(str(posDep[i][0][0])+" ("+str(posDep[i][0][1])+") - "+str(posDep[i][1])+" - "+str(posDep[i][2][0])+" ("+str(posDep[i][2][1])+" )\r\n"))
                
                for j in range(len(posDep)):
                    if(str(posDep[j][0][0])==str(posDep[i][0][0])):
                        writeFile.write(str(posDep[j][0][0])+"-"+str(posDep[j][1])+"-"+str(posDep[j][2][0])+"\r\n")
                    if(str(posDep[j][2][0])==str(posDep[i][0][0])):
                        writeFile.write(str(posDep[j][0][0])+"-"+str(posDep[j][1])+"-"+str(posDep[j][2][0])+"\r\n")
                    if(str(posDep[j][0][0])==str(posDep[i][2][0])):
                        writeFile.write(str(posDep[j][0][0])+"-"+str(posDep[j][1])+"-"+str(posDep[j][2][0])+"\r\n")
                    if(str(posDep[j][2][0])==str(posDep[i][2][0])):
                        writeFile.write(str(posDep[j][0][0])+"-"+str(posDep[j][1])+"-"+str(posDep[j][2][0])+"\r\n")
        #writeFile=open(nameOfFile, "w")
        #writeFile.write(str(treeParsed)+"\r\n\r\n")
        #print(treeParsed)
        #print("\n")
    writeFile.close()
    print("negDetector-passed") 
    
    moveDirFrom='/home/arif/Desktop/mycode/mycode5/Haydon'
    pathOfMovingFileFrom=os.path.join(moveDirFrom, str(fileSequence[fileCount])+".txt")
    
    moveDirTo='/home/arif/Desktop/mycode/mycode5/HaydonDone'
    pathOfMovingFileTO=os.path.join(moveDirTo, str(fileSequence[fileCount])+".txt")
    
    os.rename(pathOfMovingFileFrom,pathOfMovingFileTO)

           
