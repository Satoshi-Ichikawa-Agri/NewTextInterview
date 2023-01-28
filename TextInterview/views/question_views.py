from django.shortcuts import render
from django.views.generic import ListView, CreateView ,DetailView, UpdateView, DeleteView

from TextInterview.models import Question
from TextInterview.forms import QuestionForm


def home(request):
    """ GET
    Return:

    """
    return render(request, 'pages/home.html')


class QuestionIndexView(ListView):
    """ Question一覧
    QuestionテーブルからアイテムListを取得する
    指定が無ければ全データを取得し、「object_list」に格納する。
    """
    model = Question
    template_name = 'pages/index.html'


class QuestionDetailView(DetailView):
    pass


class QuestionCreateView(CreateView):
    """
    """
    model = Question
    form_class = QuestionForm # 入力フォームの指定
    success_url = '/index/' # 登録後の遷移先
    template_name = 'pages/create.html'

    def form_valid(self, form):
        """ フォームが有効だった場合の処理
        """
        return super().form_valid(form)


class QuestionUpdateView(UpdateView):
    """
    """
    pass
