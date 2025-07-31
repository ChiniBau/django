from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/create/', views.task_create, name='task-create'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login')
]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('tasks/',views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('register/', views.register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('chatbot/api/', views.chatbot_api, name='chatbot_api'),
    path('profile/', views.profile_view, name='profile'),

]