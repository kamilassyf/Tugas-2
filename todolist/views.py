from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user.username
    user_id = request.user.id
    data_todolist = Task.objects.filter(user_id=user_id)

    context = {
        'username': username,
        'todolist': data_todolist
    }
    return render(request, "todolist.html", context)  

@login_required(login_url='/todolist/login/')
def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', task), content_type='application/json')

@login_required(login_url='/todolist/login/') 
def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()  

        is_finished = False
        Task.objects.create(title=title, 
        description=description, 
        date=date, 
        user=request.user, 
        is_finished=is_finished)
        response = HttpResponseRedirect(reverse('todolist:show_todolist'))
        return response
    return render(request, "create_task.html")

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    data = Task.objects.get(id=id) 
    data.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def status(request, update_task):
    data_update = Task.objects.get(id=update_task)

    if data_update.is_finished:
        data_update.is_finished = False
    else:
        data_update.is_finished = True
    
    data_update.save() 
    return HttpResponseRedirect(reverse('todolist:show_todolist'))


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def add_ajax(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    add_todo = Task(
        user = request.user,
        title = title,
        description = description,
    )
    add_todo.save()
    return JsonResponse({"task": "todolist baru"})

@csrf_exempt
def delete_ajax(request,id):
    task = Task.objects.filter(pk=id)   
    task.delete()
    return JsonResponse({"task": "todolist dihapus"})
