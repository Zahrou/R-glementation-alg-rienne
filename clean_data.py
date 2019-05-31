import os
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JournauxOfficiels.settings")
import django
django.setup()
from app_1.models import *
import sys
import dateparser
sys.path.append("C:\\Users\\Toshiba")

wierd_characters = ["ê", "‹", "™"]

def clean_decret_presidentiel():
    for dp in decret_presidentiel.objects.all():
        objet = dp.objet
        print(objet)
        print("\n")
        objet = objet[:objet.index(".")]
        objet = objet.replace("™", "'").replace("‹", "à")
        to_be_changed = None
        try:
            to_be_changed = re.search(r'(D|d|L|l|)?(ê)(a|é|e|o|i|u|h|A|E|O|I|U|H)', objet).group(0)
        except AttributeError:
            pass
        if to_be_changed:
            new = to_be_changed.replace("ê", "'")
            objet = objet.replace(to_be_changed, new)
        objet = objet + "."
        dp.objet = objet
        dp.save()
        print(dp.objet)


# def add_to_ordonnance_t():
#     for ordo in ordonnances:
#
#         for jou in journals:
#
#             if ordo[-1] == jou.url:
#                 d = ordonnance(num=ordo[0],
#                                date=dateparser.parse(ordo[1]).date(),
#                                objet=ordo[2],
#                                journal=jou
#                                )
#                 d.save()
#
# def add_to_arrete_t():
#     for ar in arretes:
#         for jou in journals:
#             if ar[-1] == jou.url:
#                 d = arrete(num=ar[0],
#                            date=dateparser.parse(ar[1]).date(),
#                            objet=ar[2],
#                            journal=jou
#                            )
#                 d.save()
#
#
# def add_to_arrete_i():
#     for ai in arrete_i:
#         for jou in journals:
#             if ai[-1] == jou.url:
#                 d = arrete_interministeriel(num=ai[0],
#                                     date=dateparser.parse(ai[1]).date(),
#                                     objet=ai[2],
#                                     journal=jou
#                                     )
#                 d.save()
#
#
# def add_to_decision_t():
#     for dec in decisions:
#         for jou in journals:
#             if dec[-1] == jou.url:
#                 d = decision(num=dec[0],
#                              date=dateparser.parse(dec[1]).date(),
#                              objet=dec[2],
#                              journal=jou
#                             )
#                 d.save()
#


if __name__ == '__main__':
    print("cleaning decret_presidentiel...")
    clean_decret_presidentiel()
    # print("Adding to ordonance...")
    # add_to_ordonnance_t()
    # #print("Adding to arrete_interministeriel..")
    # #add_to_arrete_i()
    # print("Adding to arrete..")
    # add_to_arrete_t()
    # print("Adding to decision..")
    # add_to_decision_t()
    # print("population complete!")
