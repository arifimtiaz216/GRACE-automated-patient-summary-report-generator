#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 12:17:52 2018

@author: arif
"""
from Tkinter import *
import tkFileDialog
import os



def GUI():

    
    def quitWindow():
        os.remove("file desc2.txt")
        root.destroy()
        
    def summaryCreate():
        execfile('main2.py')
        
    def filePath():
        global glob
        
        fileName1=tkFileDialog.askopenfile()
        fileName2=str(fileName1)
        fileName3=fileName2.replace("<open file '", "")
        fileName4=fileName3.split("'")
        fileName=fileName4[0]+"\n"
        
        myFile=open("file desc2.txt","a")
        if(fileName=='None\n'):
            myFile.close()
            
        else:
            myFile.writelines(fileName)
            myFile.close()

        if(glob==4):
            Label (root, text="Added: "+fileName4[0], bg="black", fg="white", font="none 12 bold").grid(row=7,columnspan=3, sticky=N)
            glob=glob+1
        elif(glob==3):
            Label (root, text="Added: "+fileName4[0], bg="black", fg="white", font="none 12 bold").grid(row=6,columnspan=3, sticky=N)
            glob=glob+1
        elif(glob==2):
            Label (root, text="Added: "+fileName4[0], bg="black", fg="white", font="none 12 bold").grid(row=5,columnspan=3, sticky=N)
            glob=glob+1
        elif(glob==1):
            Label (root, text="Added: "+fileName4[0], bg="black", fg="white", font="none 12 bold").grid(row=4,columnspan=3, sticky=N)
            glob=glob+1
        else:
            glob=1
            
            
        print(fileName)
    
    root=Tk()
    root.title("Generate Patient Summary Form")
    root.geometry("800x400")
    root.configure(background="black")
    photo1=PhotoImage(file="acfr_logo.gif")
    Label(root, image=photo1, bg="yellow").grid(rowspan=2, columnspan=3)
    Label (root, text="\nAdd Text Files To Create Patient Summary Report:\n", bg="black", fg="white", font="none 12 bold") .grid(row=2, columnspan=3, sticky=EW)

    
    #textEntry=Entry(root, width=70, bg="white")
    #textEntry.grid(row=2, column=0)
    
    Button(root, text="ADD", width=25, command=filePath).grid(row=3,columnspan=3)
    Label (root, text="  ", bg="black", fg="black", font="none 12 bold") .grid(row=4, columnspan=3, sticky=EW)
    Label (root, text="  ", bg="black", fg="black", font="none 12 bold") .grid(row=5, columnspan=3, sticky=EW)
    Label (root, text="  ", bg="black", fg="black", font="none 12 bold") .grid(row=6, columnspan=3, sticky=EW)
    #Label (root, text="  ", bg="black", fg="black", font="none 12 bold") .grid(row=7, columnspan=3, sticky=EW)
    Button(root, text="CREATE SUMMARY", width=25, command=summaryCreate).grid(row=8,columnspan=3)
    Button(root, text="QUIT", width=15, command=quitWindow).grid(row=9,column=2, padx=5, sticky=E )
    
    

    
    root.mainloop()

glob=1
GUI()
