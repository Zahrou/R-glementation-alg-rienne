from django import template
register = template.Library()



#@register.filter(name='french_date')
def french_date(date):

    #Converts a date object to french date representation
    mois = {1: "Janvier",
            2: "Février",
            3: "Mars",
            4: "Avril",
            5: "Mai",
            6: "Juin",
            7: "Juillet",
            8: "Août",
            9: "Septembre",
            10: "Octobre",
            11: "Novembre",
            12: "Décembre",
            }

    date_in_french = "%s %s %s" % (str(date.day), mois[date.month], str(date.year))

    return date_in_french


register.filter("french_date", french_date)
