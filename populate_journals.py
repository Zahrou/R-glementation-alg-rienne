import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JournauxOfficiels.settings")
import django
django.setup()
from app_1.models import jarida, loi
import sys
sys.path.append("C:\\Users\\Toshiba")
from Populate import populate_journal, populate_decret
import dateparser

journaux = populate_journal()

def add_to_jarida():
    for n in journaux[0]:
        for url in journaux[1]:
            if journaux[0].index(n) == journaux[1].index(url):
                num = n.split("du")[0]
                date = n.split("du")[1]
                jo = jarida(num=num, date=dateparser.parse(date).date(), url=url)
                jo.save()


if __name__ == "__main__":
    print("adding to jarida..")
    add_to_jarida()
    print("population complete!")
