from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    url(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
    path('recipt/new/', views.recipe_new, name = 'recipe_new')
]