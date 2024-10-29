from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views import View
from django.contrib.auth import login as auth_login
from django.urls import reverse

from django.views.generic import TemplateView

from .forms import LoginForm
# Create your views here.

class LoginView(View):
    def get(self, request, *arg, **kwargs):
        """GETリクエスト用のメソッド"""
        context = {
            "form": LoginForm(),
        }
        return TemplateResponse(request, "accounts/login.html", context)
    
    def post(self, request, *arg, **kwargs):
        """POSTリクエスト用のメソッド"""
        #リクエストからフォームオブジェクトを作成
        form = LoginForm(request.POST)
        if not form.is_valid():
            context = {
                "form": form,
            }
            return TemplateResponse(request, 'accounts/login.html', context)
        
        user = form.get_user()
        auth_login(request, user)
        return HttpResponseRedirect(reverse('shop:index'))
    
login = LoginView.as_view()

class IndexView(TemplateView):
    template_name = "accounts/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_count'] = User.objects.count()
        return context

index = IndexView.as_view()