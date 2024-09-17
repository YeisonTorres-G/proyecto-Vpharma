from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('ayuda/', views.ayuda, name='ayuda'),
    
    path('blog/', views.blog, name='blog'),


    path('', views.product_list, name='product_list'),
    path(
        '<slug:category_slug>/',
        views.product_list,
        name='product_list_by_category'
    ),
    path(
        '<int:id>/<slug:slug>/',
        views.product_detail,
        name='product_detail'
    ),
     path('ayuda/', views.ayuda, name='ayuda'),
]

