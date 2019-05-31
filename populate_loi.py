import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JournauxOfficiels.settings")
import django
django.setup()
from app_1.models import jarida, loi
import sys
sys.path.append("C:\\Users\\Toshiba")
from Populate import populate_journal, populate_decret
import dateparser
journals = jarida.objects.order_by('date')
lois = populate_decret("Loi")

def add_to_loi():
    for L in lois:
        for jou in journals:
            if L[-1] == jou.url:
                l = loi(num=L[0], date=dateparser.parse(L[1]).date(), objet=L[2], journal=jou)
                l.save()

if __name__ == '__main__':
    print("Adding to loi...")
    add_to_loi()
    print("population complete!")
