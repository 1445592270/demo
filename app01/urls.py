from . views import  *
from django.urls import path
urlpatterns = [
    path('index/',index),
    # path('addperson/',addperson),
    path('chaxun/',chaxun),
    path('delete/', delete),
    path('update/',update),
    path('addmore/', addmore),
    path('chaxunmore/', chaxunmore),
    path('updatemore/', updatemore),
]