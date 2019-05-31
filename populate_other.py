import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JournauxOfficiels.settings")
import django
django.setup()
from app_1.models import *
import sys
sys.path.append("C:\\Users\\Toshiba")
from Populate import populate_journal, populate_decret
import dateparser
journals = jarida.objects.order_by('date')
decrets_p = populate_decret("Décret présidentiel")
ordonnances = populate_decret("Ordonnance")
arretes = populate_decret("Arrêté")
arrete_i = populate_decret("Arrêté interministériel")
decisions = populate_decret("Décision")


def add_to_decret_presidentiel():
    for dp in decrets_p:
        for jou in journals:
            if dp[-1] == jou.url:
                d = decret_presidentiel(num=dp[0],
                                    date=dateparser.parse(dp[1]).date(),
                                    objet=dp[2],
                                    journal=jou
                                    )
                d.save()


def add_to_ordonnance_t():
    for ordo in ordonnances:

        for jou in journals:

            if ordo[-1] == jou.url:
                d = ordonnance(num=ordo[0],
                               date=dateparser.parse(ordo[1]).date(),
                               objet=ordo[2],
                               journal=jou
                               )
                d.save()

def add_to_arrete_t():
    for ar in arretes:
        for jou in journals:
            if ar[-1] == jou.url:
                d = arrete(num=ar[0],
                           date=dateparser.parse(ar[1]).date(),
                           objet=ar[2],
                           journal=jou
                           )
                d.save()


def add_to_arrete_i():
    for ai in arrete_i:
        for jou in journals:
            if ai[-1] == jou.url:
                d = arrete_interministeriel(num=ai[0],
                                    date=dateparser.parse(ai[1]).date(),
                                    objet=ai[2],
                                    journal=jou
                                    )
                d.save()


def add_to_decision_t():
    for dec in decisions:
        for jou in journals:
            if dec[-1] == jou.url:
                d = decision(num=dec[0],
                             date=dateparser.parse(dec[1]).date(),
                             objet=dec[2],
                             journal=jou
                            )
                d.save()



if __name__ == '__main__':
    print("Adding to decret_presidentiel...")
    add_to_decret_presidentiel()
    print("Adding to ordonance...")
    add_to_ordonnance_t()
    print("Adding to arrete_interministeriel..")
    add_to_arrete_i()
    print("Adding to arrete..")
    add_to_arrete_t()
    print("Adding to decision..")
    add_to_decision_t()
    print("population complete!")
