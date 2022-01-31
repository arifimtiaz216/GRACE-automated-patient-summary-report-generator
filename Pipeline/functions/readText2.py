#import gui2

dummy12=gui2.getAudioStremText()
print (dummy12)
print ('#####################################')
    

# =============================================================================
# #file1 = open('../audioText.txt', mode='r')
# file1 = open('audioText.txt', mode='r')
# dummy12 = file1.read()
# file1.close()
# #print (dummy12)
# 
# =============================================================================


dummyP2=dummy12.replace(' ','%20')
dummyP3=dummyP2.replace('\'','%27')
dummyP=dummyP3.replace('&','%26')

#print dummyP

#hi='hello%20children%20how%20are%20you%20doing%20I%20am%20not%20doing%20the%20laundry%20today%20he%20went%20back%20home%20for%20sleeping.'

#stt='curl -d text=go%20home http://bark.phon.ioc.ee/punctuator'

part1='curl -d text='+dummyP+' http://bark.phon.ioc.ee/punctuator'

#print part1

import commands
op = commands.getstatusoutput(part1)

print('******************************')
#print (part1)
print('******************************')
print(op)
print('******************************')

output = op[1].rsplit('\n', 1)[1]
print (output)
print ('#####################################')

#file1= open("dummy.txt","w")
#file1.write(dummy12)
#file1.close()
