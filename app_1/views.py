import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JournauxOfficiels.settings")
import django
django.setup()
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.template import RequestContext
from app_1.models import *
from app_1.forms import *
from itertools import chain
from utilities import sort_queryset_list

# Create your views here.






def index(request):
    return render(request, "app_1/base.html")




def INDEX(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()


    if 'q' in request.GET and request.GET['q']:

        q = request.GET['q']
        if q in ["wilaya", "wilayas", "finance", "finances"]:
            err_message = "Le terme de recherche que vous avez entré n'est pas valide"
            return render(request, 'app_1/index.html', context={"err_message": err_message})
        else:
            lois = loi.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
            ordonnances = ordonnance.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
            decrets_p = decret_presidentiel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
            decrets_ex = decret_executif.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
            arre_int = arrete_interministeriel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
            arretes = arrete.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
            decisions = decision.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")


            texts_list = list(chain(lois, ordonnances, decrets_p, decrets_ex, arre_int, arretes, decisions))
            texts_list = sort_queryset_list(texts_list)

            if texts_list:
                paginator = Paginator(texts_list, 20)
                try:
                    page = int(request.GET.get('page', '1'))
                except:
                    page = 1
                try:
                    texts = paginator.page(page)
                except(EmptyPage, InvalidPage):
                    texts = paginator.page(paginator.num_pages)
                len_texts = len(texts_list)
                index = paginator.page_range.index(texts.number)
                max_index = len(list(paginator.page_range))
                start_index = index - 2 if index >= 2 else 0
                end_index = index + 2 if index <= max_index - 2 else max_index
                page_range = paginator.page_range[start_index:end_index]

                return render(request, 'app_1/index.html',
                            { 'texts' : texts,
                            'len_texts' : len_texts,
                            'q': q,
                            'parameters': parameters,
                            'page_range': page_range,
                            'lois': lois,
                            'ordonnances': ordonnances,
                            'decrets_p': decrets_p,
                            'decrets_ex': decrets_ex,
                            'arre_int': arre_int,
                            'arretes': arretes,
                            'decisions': decisions,
                            },)
            else:
                return render(request, 'app_1/index.html',
                            {
                            'q': q,
                            })
    else:

        return render(request, "app_1/index.html")




def lois_views(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    q = request.GET['q']
    lois = loi.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    ordonnances = ordonnance.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_p = decret_presidentiel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_ex = decret_executif.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arre_int = arrete_interministeriel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arretes = arrete.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decisions = decision.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    texts_list = list(chain(lois, ordonnances, decrets_p, decrets_ex, arre_int, arretes, decisions))
    texts_list = sort_queryset_list(texts_list)
    len_texts = len(texts_list)
    if texts_list:
        paginator = Paginator(texts_list, 10)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        try:
            texts = paginator.page(page)
        except(EmptyPage, InvalidPage):
            texts = paginator.page(paginator.num_pages)
        len_texts = len(texts_list)
        index = paginator.page_range.index(texts.number)
        max_index = len(list(paginator.page_range))
        start_index = index - 2 if index >= 2 else 0
        end_index = index + 2 if index <= max_index - 2 else max_index
        page_range = paginator.page_range[start_index:end_index]
    return render(request, 'app_1/resultas_lois.html', context={
                                                                   'q': q,
                                                                   'parameters': parameters,
                                                                   'lois': lois,
                                                                   'ordonnances': ordonnances,
                                                                   'decrets_p': decrets_p,
                                                                   'decrets_ex': decrets_ex,
                                                                   'arre_int': arre_int,
                                                                   'arretes': arretes,
                                                                   'decisions': decisions,
                                                                   'len_texts' : len_texts,
                                                                   })

def ordonnance_views(request):

    q = request.GET['q']
    lois = loi.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    ordonnances = ordonnance.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_p = decret_presidentiel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_ex = decret_executif.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arre_int = arrete_interministeriel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arretes = arrete.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decisions = decision.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    texts_list = list(chain(lois, ordonnances, decrets_p, decrets_ex, arre_int, arretes, decisions))
    texts_list = sort_queryset_list(texts_list)
    len_texts = len(texts_list)

    return render(request, 'app_1/resultas_ordonnances.html', context={
                                                                   'q': q,
                                                                   'lois': lois,
                                                                   'ordonnances': ordonnances,
                                                                   'decrets_p': decrets_p,
                                                                   'decrets_ex': decrets_ex,
                                                                   'arre_int': arre_int,
                                                                   'arretes': arretes,
                                                                   'decisions': decisions,
                                                                   'len_texts' : len_texts,
                                                                   })


def decrets_views(request):

    q = request.GET['q']
    lois = loi.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    ordonnances = ordonnance.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_p = decret_presidentiel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_ex = decret_executif.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arre_int = arrete_interministeriel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arretes = arrete.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decisions = decision.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    texts_list = list(chain(lois, ordonnances, decrets_p, decrets_ex, arre_int, arretes, decisions))
    texts_list = sort_queryset_list(texts_list)
    len_texts = len(texts_list)

    return render(request, 'app_1/resultas_decrets.html', context={
                                                                   'q': q,
                                                                   'lois': lois,
                                                                   'ordonnances': ordonnances,
                                                                   'decrets_p': decrets_p,
                                                                   'decrets_ex': decrets_ex,
                                                                   'arre_int': arre_int,
                                                                   'arretes': arretes,
                                                                   'decisions': decisions,
                                                                   'len_texts' : len_texts,
                                                                   })


def decrets_presidentiel_view(request):

    q = request.GET['q']
    lois = loi.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    ordonnances = ordonnance.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_p = decret_presidentiel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_ex = decret_executif.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arre_int = arrete_interministeriel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arretes = arrete.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decisions = decision.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    texts_list = list(chain(lois, ordonnances, decrets_p, decrets_ex, arre_int, arretes, decisions))
    texts_list = sort_queryset_list(texts_list)
    len_texts = len(texts_list)

    return render(request, 'app_1/decrets_presidentiel.html', context={
                                                                   'q': q,
                                                                   'lois': lois,
                                                                   'ordonnances': ordonnances,
                                                                   'decrets_p': decrets_p,
                                                                   'decrets_ex': decrets_ex,
                                                                   'arre_int': arre_int,
                                                                   'arretes': arretes,
                                                                   'decisions': decisions,
                                                                   'len_texts' : len_texts,
                                                                   })

def arre_int_view(request):

    q = request.GET['q']
    lois = loi.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    ordonnances = ordonnance.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_p = decret_presidentiel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_ex = decret_executif.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arre_int = arrete_interministeriel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arretes = arrete.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decisions = decision.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    texts_list = list(chain(lois, ordonnances, decrets_p, decrets_ex, arre_int, arretes, decisions))
    texts_list = sort_queryset_list(texts_list)
    len_texts = len(texts_list)

    return render(request, 'app_1/arretes_interministeriels.html', context={
                                                                   'q': q,
                                                                   'lois': lois,
                                                                   'ordonnances': ordonnances,
                                                                   'decrets_p': decrets_p,
                                                                   'decrets_ex': decrets_ex,
                                                                   'arre_int': arre_int,
                                                                   'arretes': arretes,
                                                                   'decisions': decisions,
                                                                   'len_texts' : len_texts,
                                                                   })
def arrete_view(request):

    q = request.GET['q']
    lois = loi.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    ordonnances = ordonnance.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_p = decret_presidentiel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_ex = decret_executif.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arre_int = arrete_interministeriel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arretes = arrete.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decisions = decision.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    texts_list = list(chain(lois, ordonnances, decrets_p, decrets_ex, arre_int, arretes, decisions))
    texts_list = sort_queryset_list(texts_list)
    len_texts = len(texts_list)

    return render(request, 'app_1/resultas_arretes.html', context={
                                                                   'q': q,
                                                                   'lois': lois,
                                                                   'ordonnances': ordonnances,
                                                                   'decrets_p': decrets_p,
                                                                   'decrets_ex': decrets_ex,
                                                                   'arre_int': arre_int,
                                                                   'arretes': arretes,
                                                                   'decisions': decisions,
                                                                   'len_texts' : len_texts,
                                                                   })

def decision_view(request):

    q = request.GET['q']
    lois = loi.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    ordonnances = ordonnance.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_p = decret_presidentiel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decrets_ex = decret_executif.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arre_int = arrete_interministeriel.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    arretes = arrete.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    decisions = decision.objects.filter(Q(num__iexact=q) | Q(objet__icontains=q)).order_by("-date")
    texts_list = list(chain(lois, ordonnances, decrets_p, decrets_ex, arre_int, arretes, decisions))
    texts_list = sort_queryset_list(texts_list)
    len_texts = len(texts_list)

    return render(request, 'app_1/resultas_decisions.html', context={
                                                                   'q': q,
                                                                   'lois': lois,
                                                                   'ordonnances': ordonnances,
                                                                   'decrets_p': decrets_p,
                                                                   'decrets_ex': decrets_ex,
                                                                   'arre_int': arre_int,
                                                                   'arretes': arretes,
                                                                   'decisions': decisions,
                                                                   'len_texts' : len_texts,
                                                                   })

















# def search_filters(request):
#     get_copy = request.GET.copy()
#     parameters = get_copy.pop('page', True) and get_copy.urlencode()
#     q = request.GET['q']
#     lois = SearchQuerySet()#.autocomplete(content_auto=request.GET.get('search_text', ''))
#     return render(request, "app_1/search.html", context={"lois": lois})
