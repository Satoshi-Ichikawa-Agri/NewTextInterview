""" textInterviewApp
<使う場面>
会員登録、お問い合わせ、Webサイトへ来てくれた人に入力/選択してもらうとき、
Webサイトへ来てくれた人からの情報をデータ保存したいとき

"""
from django import forms
from django.contrib.auth import get_user_model

from .models import *

class QuestionForm(forms.ModelForm):
    """ Qestionのフォーム
    """
    title = forms.CharField(max_length=50, label="カテゴリ")
    question_content = forms.CharField(max_length=100, label="質問")
    answer = forms.CharField(widget=forms.Textarea(), max_length=4000, label="回答")

    class Meta:
        model = Question
        fields = '__all__'


class UserCreationForm(forms.ModelForm):
    """ Userのフォーム
    """
    password = forms.CharField()
 
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', )
 
    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password
 
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

