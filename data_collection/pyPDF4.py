# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 18:37:41 2018

@author: Zahreddine
"""

from os import chdir, getcwd, listdir, path
from PyPDF2 import PdfFileWriter, PdfFileReader 
import re
from joradp3 import get_urllist

pdf0 = "http://www.joradp.dz/FTP/JO-FRANCAIS/"
years = get_urllist()[1]
chdir("D:/Desktop/Journal officiel2/2003")


def get_string(fichier):
    
    num_journal = fichier[12:fichier.index('.')]
    journal_url = pdf0 + fichier[8:12] + "/F" + fichier[8:]
    
    
    with open (fichier, "rb") as file:
        conte = PdfFileReader(file)
    
        jo = """
                """
        for i in range(conte.getNumPages()):
            try:
                if i == 0:
                    page1 = conte.getPage(i).extractText()
                    page1 = page1.replace("  ", " ")
                    year = fichier[8:12]
                    
                    to_strip = "%sème ANNEE" % str(years.index(int(year))+1)
                    to_strip_two = "%sè ANNEE" % str(years.index(int(year))+1)
                    page1 = page1.replace("”", "é").replace("’", "ê").replace("‘", "è").replace("Õ", "'").replace(to_strip, '').replace(to_strip_two, "")
                    date = re.search(r'(Dimanche|Samedi|Lundi|Mardi|Mercredi|Jeudi|Vendredi)?(\w|\s)*(1|2)?([0-9]{1})?(\w|\s)*1[0-9]{3}(\s)*(correspondant|Correspondant)(\w|\s)*(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)(\w|\s|\d)*(1|2)[0-9]{3}', page1).group(0)
                    date = date.lower()
                    date_hijri =  date.split("correspondant au")[0].strip()
                    date_grigorian =  date.split("correspondant au")[1].strip()
            
            except :
                date_hijri =  "Date hijri n'a pas pu être récupérée"
                date_grigorian =  "Date n'a pas pu être récupérée"
            
            page = conte.getPage(i)
            #print(str(i)+"\n" + page.extractText() + "\n")
            jo += page.extractText()
        
        sommaire = ""
        
        try:
            sommaire = jo[:jo.rindex("S O M M A I R E")]
        except ValueError:
            try:
                sommaire = jo[:jo.rindex("SOMMAIRE")]
            except ValueError:
                pass
         
    
                     
            
    return jo, sommaire, num_journal, journal_url, page1, date_grigorian, date_hijri




class journalOfficiel:
    
    
    list_des_texts = {"Loi":["Loi", "Lois"], 
                      "Ordonnance": ["Ordonnance", "Ordonnances"], 
                      "Décret présidentiel": ["Décret présidentiel", "Décrets présidentiels"],
                      "Décret exécutif": ["Décret exécutif", "Décrets exécutifs"], 
                      "Arrêté interministériel": ["Arrêté interministériel", "Arrêtés interministériels"], 
                      "Arrêté n°": ["Arrêté n°", "Arrêtés n°"], 
                      "Arrêté du": ["Arrêté du", "Arrêtés du"], 
                      "Décision interministérielle": ["Décision interministérielle", "Décisions interministérielles"], 
                      "Décision n°": ["Décision n°", "Décisions n°"], 
                      "Décision du": ["Décision du", "Décisions du"],
                     }

    def __init__(self, fichier, journal):
        
        """
        Rénitier le journal objet.
        prend un journal officiel comme une chaine de caractères.
        le journal objet a deux attribues:
                - self.journal (le journal officiel en chaine de caractères).
                - self.sommaire (renvoyé par la fonction get_string).
        """
        self.texts = {
                        "Loi": [],
                        "Ordonnance": [],
                        "Décret présidentiel": [],
                        "Décret exécutif": [],
                        "Arrêté interministériel": [],
                        "Arrêté": [],
                        "Décision interministérielle": [],
                        "Décision": [],
                    }
        self.fichier = fichier
        self.journal = journal
        self.sommaire = get_string(fichier)[1]
        self.num_journal = get_string(fichier)[2][1:]
        self.date_journal = get_string(fichier)[5]
        self.date_journal_hijri = get_string(fichier)[6]
        self.journal_url = get_string(fichier)[3]
    
    
    
    
    def construir_journal(self):
        
        if len(self.journal) > 100:

            self.sommaire = self.sommaire.replace('  ', ' ')
            self.sommaire = self.sommaire.replace('\n', ' ')
            
            if "”" in self.sommaire or "‘" in self.sommaire or "Õ" in self.sommaire or "’" in self.sommaire:
                self.sommaire = self.sommaire.replace("”", "é").replace("’", "ê").replace("‘", "è").replace("Õ", "'")    
            
            for T in journalOfficiel.list_des_texts:
                for t in journalOfficiel.list_des_texts[T]:
                    
                
                    for i in range(len(self.sommaire)):
                        
                        if self.sommaire[i: i+len(t)] == t :
                            
                            string = ""
                            journal1 = self.sommaire[i:]
                            for y in range(len(journal1)):
                                string += journal1[y]
                                if journal1[y:y+3] == "..."  :
                                    break
                                elif len(string) > 5:
                                    if journal1[y:y+len("Loi")] == "Loi" or journal1[y:y+len("Ordonnance")] == "Ordonnance" or journal1[y:y+len("Décret présidentiel")] == "Décret présidentiel" or journal1[y:y+len("Décret exécutif")] == "Décret exécutif" or journal1[y:y+len("Arrêté")] == "Arrêté" or journal1[y:y+len("Décision")] == "Décision" or journal1[y:y+len("MINISTERE")] == "MINISTERE" or journal1[y:y+len("ARRETES")] == "ARRETES" or journal1[y:y+len("DECRETS")] == "DECRETS" or journal1[y:y+len("LOS")] == "LOIS" or journal1[y:y+len("ORDONNACES")] == "ORDONNANCES" or journal1[y:y+len("ACCORDS")] == "ACCORDS" or journal1[y:y+len("CONVENTIONS")] == "CONVENTIONS"  :
                                        string = string.strip(journal1[y])
                                        break
                            if "du" in T or "n°" in T:
                                                    
                                self.texts[T[:-3]].append(string)
                            else:
                                self.texts[T].append(string)
             
                    
                    
        
        #return self.texts
                
    def get_text(self, text):
        
        
        """ 
        Prend un text réglomentaire en argument
        Renvoie une list des textes cherchés qui existent dans le journal officiel
        
        """
        return self.texts[text]
    
    