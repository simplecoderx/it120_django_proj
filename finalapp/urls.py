from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index,name='index'),
    path('', base_view),
    path('add', add,name='add'),
    path('delete/<int:myid>', delete,name='delete'),
    path('edit/<int:myid>', edit,name='edit'),
    path('update/<int:myid>', update,name='update'),
    path('view/<int:myid>', view,name='view'),
    path('back/<int:myid>', back,name='back'),
    path('search', search,name='search-item'),
]