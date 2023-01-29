from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from TextInterview.models import PersonalInformation
from TextInterview.forms import UserCreationForm
 
 
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'pages/signup.html'
 
    def form_valid(self, form):
        return super().form_valid(form)
 
 
class Login(LoginView):
    template_name = 'pages/login.html'
 
    def form_valid(self, form):
        return super().form_valid(form)
 
    def form_invalid(self, form):
        return super().form_invalid(form)
 
 
class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'pages/account.html'
    fields = ('username', 'email',)
    success_url = '/account/'
 
    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()
 
 
class PersonalInfoUpdateView(LoginRequiredMixin, UpdateView):
    model = PersonalInformation
    template_name = 'pages/personalInfo.html'
    fields = ('name', 'zipcode', 'prefecture',
              'city', 'address1', 'address2', 'tel')
    success_url = '/personalInfo/'
 
    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()
