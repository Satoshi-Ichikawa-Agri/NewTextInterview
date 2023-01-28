from django.shortcuts import render
from django.views.generic import ListView, DetailView

from TextInterview.models import Question


def home(request):
    """ GET
    Return:

    """
    return render(request, 'pages/home.html')


class IndexListView(ListView):
    """ 質問index
    ItemテーブルからアイテムListを取得する
    指定が無ければ全データを取得し、「object_list」に格納する。
    """
    model = Question
    template_name = 'pages/index.html'

