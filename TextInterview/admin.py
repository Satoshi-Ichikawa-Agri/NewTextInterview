from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from TextInterview.models import Question
from TextInterview.forms import *


admin.site.register(Question)

admin.site.unregister(Group) # 管理画面から非表示
