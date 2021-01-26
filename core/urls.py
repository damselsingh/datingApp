from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
   path('', views.home, name='homepage'),
   path('login/', views.user_login.as_view(), name='login'),
   path('feeds/', views.feeds, name='feeds'),
   path('logout/', views.user_logout.as_view(), name='logout'),
   path('signup/', views.user_signup.as_view(), name='signup'),
   path('my-profile/', views.my_profile, name='profile'),
   path('profile-edit/<int:id>/', views.profile_edit, name='profiledit'),
   path('user-profile-settings/', views.user_profile_settings, name='user-settings')
]
