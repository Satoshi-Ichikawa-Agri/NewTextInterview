"""
TextInterViewAppで使用するルーティングを定義する。
プロジェクト本体のUrlsファイルでは読込だけ。
"""
from django.urls import path

from TextInterview.views import *


urlpatterns = [
    path('', question_views.TopPageView.as_view(), name='home'),
    path('index/', question_views.QuestionIndexView.as_view(), name='index'),
    path('create/', question_views.QuestionCreateView.as_view(), name='create'),
    path('update/<str:pk>/', question_views.QuestionUpdateView.as_view(), name='update'),
    path('delete/<str:pk>/', question_views.QuestionDeleteView.as_view(), name='delete'),
]
