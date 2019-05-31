# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 18:35:28 2017

@author: Toshiba
"""

import pyPDF4

jo = pyPDF4.journalOfficiel("Jouranl 2007029.pdf", pyPDF4.get_string("Jouranl 2007029.pdf")[0])

text_types = {"Loi":["Loi", "Lois"], 
              "Ordonnance": ["Ordonnance", "Ordonnances"], 
              "Décret exécutif": ["Décret exécutif", "Décrets exécutifs", "Décretexécutif", "Décretsexécutifs"], 
              "Décret présidentiel": ["Décret présidentiel", "Décrets présidentiels", "Décretprésidentiel", "Décrets présidentiels"],
              "Arrêté interministériel": ["Arrêté interministériel", "Arrêtés interministériels", "Arrêtéinterministériel"],  
              "Arrêté": ["Arrêté du", "Arrêtés du", "Arrêtédu", "Arrêtésdu"], 
              "Décision interministérielle": ["Décision interministérielle", "Décisions interministérielles", "Décisioninterministérielle", "Décisionsinterministérielles"], 
              "Décision": ["Décision n°", "Décisions n°", "Décision du", "Décisions du", "Décisionn°", "Décisionsn°", "Décisiondu", "Décisionsdu"], 
              
             }
jo.construir_journal()
journal = jo.journal.replace("  ", " ")
for text in text_types:
    len_text = len(jo.texts[text])
    count_text = 0
    for t in text_types[text]:
        count_text += int(journal.count(t)/2)
    print(text, "-->",len_text, "vs", count_text)
    
    
