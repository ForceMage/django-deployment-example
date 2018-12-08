from django.urls import path
from myapp import views

# SET THE NAMESPACE!
app_name = 'myapp'

# Be careful setting the name to just /login use user_login instead!
urlpatterns=[
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
