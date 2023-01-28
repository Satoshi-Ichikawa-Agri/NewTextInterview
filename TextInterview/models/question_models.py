""" 仮questionモデル
面接官からの質問集と回答者の回答を収録する。
"""
from django.db import models


class Question(models.Model):
    """
    """
    title = models.CharField(max_length=50)
    question_content = models.CharField(max_length=100)
    answer = models.CharField(max_length=4000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Pythonデフォルトのクラスメソッド
        selfとはクラスのインスタンス
        strを返す※returnは文字列であること
        Return:
            Itemクラスの「name」
        """
        return self.question_content
