from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .forms import HelloForm, MessageForm
from .models import Rank, Message
from django.db.models import QuerySet, Q, Count, Sum, Avg
from . forms import FindForm, CheckForm
from django.core.paginator import Paginator

# Create your views here.

def index(request, num=1):
    
    data = Rank.objects.all()
    page = Paginator(data, 3)
    params = {
        'title': '真壁瑞希',
        'msg': '',
        'data': page.get_page(num),
        }
    
    return render(request, 'proto/index.html', params)

def create(request):

    if (request.method == 'POST'):
        obj = Rank()
        rank = HelloForm(request.POST, instance=obj)
        rank.save()
        return redirect(to='/proto')
    params = {
        'title':'真壁瑞希',
        'form': HelloForm(),
    }
    return render(request, 'proto/create.html', params)

def edit(request, num):
    obj= Rank.objects.get(id=num)
    if (request.method == 'POST'):
        rank = HelloForm(request.POST, instance=obj)
        rank.save()
        return redirect(to='/proto')
    params = {
        'title':'HELLO',
        'id':num,
        'form': HelloForm(instance=obj),
    }
    return render(request, 'proto/edit.html', params)

def delete(request, num):
    rank = Rank.objects.get(id=num)
    if (request.method == 'POST'):
        rank.delete()
        return redirect(to='/proto')
    params = {
        'title':'真壁瑞希',
        'id':num,
        'obj': rank,
    }
    return render(request, 'proto/delete.html', params)

class RankList(ListView):
    model = Rank
class RankDetail(DetailView):
    model = Rank

def find(request):
    if (request.method == 'POST'):
        form = FindForm(request.POST)
        msg = request.POST['find']
        sql = 'select * from proto_rank'
        if (msg != ''):
            sql += ' where ' + msg
        data = Rank.objects.raw(sql)
        msg = sql
    else:
        msg = '検索フォーム'
        form = FindForm()
        data = Rank.objects.all()
    params = {
        'title':'真壁瑞希',
        'message':'checking',
        'form':HelloForm(),
        'data':data,
    }
    return render(request, 'proto/find.html', params)

def check(request):
    params = {
        'title':'Hello',
        'message':'check validation',
        'form': CheckForm(),
    }
    if (request.method == 'POST'):
        obj = Rank()
        form = HelloForm(request.POST, instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'try again'

        
    return render(request, 'proto/check.html', params)

def message(request, page=1):
    if (request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'proto/message.html', params)


