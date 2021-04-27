from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ConectForm, SearchForm, Add, LoginForm
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from .models import Datasample, UploadFile
from django.views import generic
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView) 

# Create your views here.

def sample(request):
    params = {
        'title':'真壁瑞希',
        'msg1':'djangoを紹介しつつ、このサイトを作った際の開発環境を載せております',
        'msg2':'このページではdjangoを利用するメリットをわかりやすく解説しております',
        'msg3':'djangoの機能の一つであるデータベースのサンプルを載せております。',
        'msg4':'ログイン画面、データのアップロードのデモです。',
        'msg5':'pythonを中心に作ったプログラムを載せております。一部ダウンロードあり',
        'msg6':'お問い合わせはこちらに。',
        'form':'form',
    }
    
    return render(request, 'port1/sample.html', params)
    

def form(request):
    
    
    params = {
        'title':'真壁瑞希',
        'msg':'お問い合わせ用フォーム',
        'sample':'sample',
        'form':ConectForm(),        
    }
    if request.method == 'POST':
        fork = ConectForm(request.POST)
        
        if fork.is_valid():
            
            subject = fork.cleaned_data['subject']
            name = fork.cleaned_data['name']
            from_mail = fork.cleaned_data['mail']
            message = fork.cleaned_data['text']
            recipients = [settings.EMAIL_HOST_USER]
            
            message = message + '<br>お名前：　' +name+ '<br>メールアドレス：　' +from_mail
            
            send_mail(subject, message, from_mail, recipients, html_message=message)
            return redirect('post_ok')
            
       
        
    return render(request, 'port1/form.html', params)


def post_ok(request):
    
    return render(request, 'port1/post_ok.html')

def creates(request):

    obj = Datasample()
    add = Add(request.POST, instance=obj)
    if add.is_valid():
        add.save()
        return redirect('database')
    else:
        return render(request, 'port1/path.html')
    
def database(request):
    data = Datasample.objects.all()
    if (request.method == 'POST'):
        form = SearchForm(request.POST) #fo-m
        search = request.POST['search'] #input
        if Datasample.objects.filter(name=search).exists():
            data = Datasample.objects.filter(name=search) 
        else:
            data = Datasample.objects.all()
    else:
        form = SearchForm()
        data = Datasample.objects.all()
    params = {
        'title':'Djangoでのデータベース',
        'data':data,
        'form':form,
        'message':'追加フォーム',
        'message1':'検索フォーム',
        'form_add':Add(),
        
    }
    return render(request, 'port1/database.html', params)
    
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'port1/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'login.html'

def login_ok(request):
    return render(request, 'port1/login_ok.html')


def link(request):
    file_obj = UploadFile.objects.all()
    return render(request, 'port1/link.html', {'file_obj': file_obj})

def introduction(request):
    return render(request, 'port1/introduction.html')
def merit(request):
    return render(request, 'port1/merit.html')
def path(request):
    return render(request, 'port1/path.html')