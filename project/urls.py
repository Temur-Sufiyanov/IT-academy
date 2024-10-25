from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('projects_add/', views.project_add, name ='project_add'),
    path('projects_edit/<uuid:id>', views.projects_edit, name ='projects_edit'),
    path('projects_searchbar/', views.projects_searchbar, name ='projects_searchbar'),
    path('projects_delete/<uuid:id>', views.projects_delete, name ='projects_delete'),
    path('<uuid:id>', views.project, name ='project'),
    
]