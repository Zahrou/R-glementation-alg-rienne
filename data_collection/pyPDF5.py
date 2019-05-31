# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 00:29:18 2017

@author: Toshiba
"""

from os import chdir, getcwd, listdir, path

from PyPDF2 import PdfFileWriter, PdfFileReader 
import re

chdir("D:/Desktop/Journal officiel/2017")

file = open("Jouranl 2017-17.pdf", "rb")




conte = PdfFileReader(file)

#page = conte.getPage(3)
#
#text = page.extractText()


text = """
        """

for i in range(conte.getNumPages()):
    page = conte.getPage(i)
    text += page.extractText()



texts = {
        "lois": [],
        "ordonnances": [],
        "decrets présidentiels": [],
        "decrets executif": [],
        "arrêtés interministeriels": [],
        "arrêtés": [],
        "décisions interministeriels": [],
        "décisions": [],
        }
        

text2 = text[:text.rindex("DECRETS")]
def get_texts(text):
    
    
    
    for i in range(len(text)):
        if text[i: i+len("Décret exécutif")] == "Décret exécutif":
            print("decret was found")
            
            decret_executif = ""
            text4 = text[i:]
            for x in range(len(text4)):
                decret_executif += text4[x]
                decret_executif
                
                if text4[x:x+3] == "...":
                    break
            decret_executif = decret_executif[:-2]
            texts["decrets executif"].append(decret_executif)
            
        


#for i in range(len(text)):
#    
#    if text[:i].count("DECRETS") >= 3:
#        print(text.index(text[i]))
#        break
            
        
        

            
            
            
            
            
            
            
            
            
            