import datetime
from haystack import indexes
from app_1.models import loi, decret_executif, decret_presidentiel


class loi_index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    date = indexes.DateField(model_attr="date")
    content_auto = indexes.EdgeNgramField(model_attr="num")
    content_auto = indexes.EdgeNgramField(model_attr="objet")


    def get_model(self):
        return loi

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
