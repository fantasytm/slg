from django.urls import path

from . import views

urlpatterns = [
    path('login', views.user_login),
    path('test', views.account_test),
    path('bind', views.bind_account),
    path('enter/game', views.enter_game),
]