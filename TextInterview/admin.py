from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from TextInterview.models import Question, User, PersonalInformation
from TextInterview.forms import QuestionForm, UserCreationForm


class PersonalInfoInline(admin.StackedInline):
    model = PersonalInformation
    can_delete = False
 
 
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        (None, {'fields': ('is_active', 'is_admin',)}),
    )
    list_display = ('username', 'email', 'is_active',)
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'is_active',)}),
    )
    add_form = UserCreationForm
    inlines = (PersonalInfoInline,)


admin.site.register(Question)
admin.site.register(User, CustomUserAdmin)

admin.site.unregister(Group) # 管理画面から非表示
