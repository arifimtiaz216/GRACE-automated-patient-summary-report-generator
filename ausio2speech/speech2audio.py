import speech_recognition as sr

import os
import os.path

folder='/home/arif/Desktop/mycode/audio2speech/Haydons Recordings/24 Janurary 2019/Original'
folderN='/home/arif/Desktop/mycode/audio2speech/Haydons Recordings/24 Janurary 2019/Original Narratives'

count=0
#fileContents=[]
fileSequence=[]

for filename in os.listdir(folder):
    
    count=count+1
    #print(str(count)+" filename->"+filename[:-4])
    
    filepath=os.path.join(folder,filename)
    #print(str(count)+" filepath->"+filepath)
    
    fileSequence.append(filename[:-4]) #FOR WAV
    #fileSequence.append(filename[:-5]) #FOR FLAC
    
#print(fileSequence)
#os.chdir(folder)
#print(os.getcwd())
    
for i in range(0,len(fileSequence)):
    r = sr.Recognizer()
    nameOfFile = fileSequence[i]
    audio = str(nameOfFile)+'.wav'
    
    #print(nameOfFile)
    #print(audio)
    
    os.chdir(folder)
    with sr.AudioFile(audio) as source:
        #print('Hello There !')
        audio = r.listen(source)
        print('Started !')
        
    try:
        text = r.recognize_google(audio)
        os.chdir(folderN)
        file = open(nameOfFile+".txt", "w")
        file.write(text)
        print(text)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        file.close()
    except Exception as e:
        print("Exception is :"+str(e))
