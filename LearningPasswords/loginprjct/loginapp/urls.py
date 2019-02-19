from django.conf.urls import url
from loginapp import views

#template NAME
app_name='loginapp'


urlpatterns=[
    url('register',views.register,name='register'),
    url('login',views.login,name='login'),

]
