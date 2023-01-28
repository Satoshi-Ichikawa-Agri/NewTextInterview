""" textInterviewApp
<使う場面>
会員登録、お問い合わせ、Webサイトへ来てくれた人に入力/選択してもらうとき、
Webサイトへ来てくれた人からの情報をデータ保存したいとき

"""
from django import forms
from django.contrib.auth import get_user_model

from .models import *

class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=50, label="カテゴリ")
    question_content = forms.CharField(max_length=100, label="質問")
    answer = forms.CharField(widget=forms.Textarea(), max_length=4000, label="回答")

    class Meta:
        model = get_user_model()
        fields = '__all__'

