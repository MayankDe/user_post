from django.urls import path
from User import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('post/',views.post,name='post')


]