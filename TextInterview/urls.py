"""
TextInterViewAppで使用するルーティングを定義する。
プロジェクト本体のUrlsファイルでは読込だけ。
"""
from django.urls import path

from TextInterview.views import *


urlpatterns = [
    path('', question_views.home),
    path('index/', question_views.IndexListView.as_view()),
]
