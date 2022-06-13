from django.urls import path
from . import views
app_name='chocolate_app'

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('shop',views.shop,name='shop'),
    path('confirm', views.confirm, name='confirm'),

]