from django.urls import include, path
from app_1 import views

app_name = "app_1"
urlpatterns = [
    path('', views.index, name = "index"),
    path('search/', views.INDEX, name = "results"),
    path('search/decrets-executifs', views.decrets_views, name = "decret_executif"),
    path('search/decrets-presidentiels', views.decrets_presidentiel_view, name = "decret_presidentiel"),
    path('search/lois', views.lois_views, name = "lois"),
    path('search/ordonnances', views.ordonnance_views, name = "ordonnances"),
    path('search/arretes-interministeriels', views.arre_int_view, name = "arretes_interministeriels"),
    path('search/arretes', views.arrete_view, name = "arretes"),
    path('search/decisions', views.decision_view, name = "decision"),
    ]
