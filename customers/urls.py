from django.urls import path
from .import views

urlpatterns = [
    path('account/',views.show_account, name='account')



]
