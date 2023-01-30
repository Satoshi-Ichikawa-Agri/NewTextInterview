"""
TextInterViewAppで使用するルーティングを定義する。
プロジェクト本体のUrlsファイルでは読込だけ。
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView # Logoutのviewsはdjangoから引用

from TextInterview.views import *


urlpatterns = [
    path('', question_views.TopPageView.as_view(), name='home'),
    path('index/', question_views.QuestionIndexView.as_view(), name='index'),
    path('create/', question_views.QuestionCreateView.as_view(), name='create'),
    path('update/<str:pk>/', question_views.QuestionUpdateView.as_view(), name='update'),
    path('delete/<str:pk>/', question_views.QuestionDeleteView.as_view(), name='delete'),
    path('login/', account_views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', account_views.SignUpView.as_view(), name='signup'),
    path('account/', account_views.AccountUpdateView.as_view(), name='account'),
    path('personalInfo/', account_views.PersonalInfoUpdateView.as_view(), name='personalInfo'),
    path('simIndex/', simulation_views.SimulationIndexView.as_view(), name='simIndex'),
    path('simulation/', simulation_views.SimulationView.as_view(), name='simulation'),
]
