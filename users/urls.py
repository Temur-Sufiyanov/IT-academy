from django.urls import path
import uuid
from . import views



urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('login/', views.login_user, name='login'),
    path('account/', views.account_user, name='account'),
    path('account_skill_change/<uuid:id>/', views.account_skill_change, name='account_skill_change'),
    path('account_skill_delete/<uuid:id>/', views.account_skill_delete, name='account_skill_delete'),
    path('account_skill_add/', views.account_skill_add, name='account_skill_add'),
    path('account_searchbar/', views.account_searchbar, name ='account_searchbar'),
    path('account_edit/', views.account_edit, name='account_edit'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<uuid:pk>/', views.profile, name='profile'),
]
