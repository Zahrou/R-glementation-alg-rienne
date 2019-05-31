import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JournauxOfficiels.settings")
import django
django.setup()
from app_1.models import jarida, loi, decret_executif
import sys
sys.path.append("C:\\Users\\Toshiba")
from Populate import populate_journal, populate_decret
import dateparser
journals = jarida.objects.order_by('date')
decrets = populate_decret("Décret exécutif")

def add_to_decret_executif():
    for de in decrets:
        for jou in journals:
            if de[-1] == jou.url:
                d = decret_executif(num=de[0], date=dateparser.parse(de[1]).date(), objet=de[2], journal=jou)
                d.save()

if __name__ == '__main__':
    print("Adding to decret_executif...")
    add_to_decret_executif()
    print("population complete!")
