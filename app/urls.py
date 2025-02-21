from django.urls import path
from .views import userView,userNamevalidateView,pwdvalidate,match_password


urlpatterns =[
    path('userform/',userView,name='userForm'),
    path('uservalidate/',userNamevalidateView,name='userNameValidate'),
    path('pwdvalidate/',pwdvalidate,name='pwdValidate'),
    path('matchpwd/',match_password,name='matchPassword'),
]
