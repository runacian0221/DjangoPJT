from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accountapp.views import AccountCreateView, hello_world

app_name = 'accountapp'

# name을 사용하면 'accountapp:hello_world' 이런 방식으로도 호출이 가능하다.

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
]