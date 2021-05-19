from django.urls import path
from . import views


urlpatterns = [
    path('branches/', views.search),
    path('branches/autocomplete/', views.autocomplete),
    path('bank_list',views.bank_list),
    path('',views.give_format),
]
