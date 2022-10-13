from django.urls import path
from todolist.views import delete_task, show_todolist,register, login_user,logout_user,create_task,status,delete_task,show_json, add_ajax, delete_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('create_task/', create_task, name='create_task'),
    path('status/<int:update_task>', status, name='status'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('json/', show_json, name='show_json'),
    path('add_ajax/', add_ajax, name='add_ajax'),
    path('delete/<int:id>/', delete_ajax, name='delete_ajax'),
]