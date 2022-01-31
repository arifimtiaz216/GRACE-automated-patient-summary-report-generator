#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:48:56 2019

@author: arif
"""
from pydub import AudioSegment

sound1main=AudioSegment.from_wav("/home/arif/Desktop/mycode/audio2speech/audio2speechV2/myTested/A_insertedNoise24JanHaydonRecordingsWithModifiedrateAudios/000_190105.wav")
sound2bg=AudioSegment.from_wav("/home/arif/Desktop/mycode/audio2speech/audio2speechV2/myTested/A_insertedNoise24JanHaydonRecordingsWithModifiedrateAudios/sirenvehicle.wav")

#combined=sound1main.overlay(sound2bg)

#combined.export("/home/arif/Desktop/mycode/audio2speech/audio2speechV2/myTested/A_insertedNoise24JanHaydonRecordingsWithModifiedrateAudios/combined.wav",format='wav')

l1=len(sound1main)
l2=len(sound2bg)
f=float(l1)/float(l2)

sound2bg=sound2bg * 2

print(sound1main.dBFS)
print(sound2bg.dBFS)

sound2bg = sound2bg - 12
print(sound2bg.dBFS)

l2=len(sound2bg)

#print(l1, l2, f)
combined=sound1main.overlay(sound2bg, times=5)

combined.export("/home/arif/Desktop/mycode/audio2speech/audio2speechV2/myTested/A_insertedNoise24JanHaydonRecordingsWithModifiedrateAudios/combined.wav",format='wav')
print("Done!")