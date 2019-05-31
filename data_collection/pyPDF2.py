# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:35:11 2017

@author: Toshiba
"""

import os

from os import chdir, getcwd, listdir, path

from PyPDF2 import PdfFileWriter, PdfFileReader 


chdir("D:/Desktop/Journal officiel/2017")

file = open("Jouranl 2017-17.pdf", "rb")

conte = PdfFileReader(file)

page = conte.getPage(3)

text = page.extractText()
text2 = " "
for x in text:
    if x != "Š":
        text2 += x
    else :
        text2 += "\nŠŠŠŠ\n"
#print(text2)        
decret = []
p =""

for a,b in enumerate(text2):

    if b == "D":

        p = text2[a : a+15]
        p +=" "+str(a)
        decret.append(p)

for x in decret :
    if x[:15] == 'Décret exécutif':
        print(x)
print(decret)
