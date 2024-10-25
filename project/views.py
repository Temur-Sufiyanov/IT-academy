from django.shortcuts import render, redirect
from .models import *
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def projects(request):
    
    reviews_p = Review.objects.filter(value="+")
    reviews_m = Review.objects.filter(value="-")
    projects = Project.objects.filter(project_review__isnull=True)
    paginator = Paginator(projects, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'reviews_p':reviews_p,
        'reviews_m':reviews_m,
    }
    return render(request, 'project/projects.html', context)


def project(request, id):
    project = Project.objects.get(id=id)
    tags = project.tag.all()
    # comments = project.comment_set.all()
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = Comment(body=form.cleaned_data['body'], user=request.user, post_name=project)
    #         comment.save()
    #         return redirect('project', id = project.id)
    # else:
    #     form = CommentForm()
    context = {
        'project': project,
        'tags': tags,
        # 'comments':comments,
        # 'form':form,
    }
    return render(request, 'project/project.html', context)

@login_required(login_url='/login/')
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user.profil
            project.save()
            messages.success(request, "Loyiha muvafaqiyatli yaratildi")
            return redirect('projects')
    else:
        form = ProjectForm()
    context = {
        'form':form,
    }
    return render(request, 'project/project_add.html', context)

@login_required(login_url='/login/')
def projects_edit(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES ,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'form':form,
    }
    return render(request, 'project/project_add.html', context)

@login_required(login_url='/login/')
def projects_delete(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Loyiha muvafaqiyatli o'chirildi")
        return redirect('projects')
    
    context = {
        'project':project,
    }

    return render(request, 'project/project_delete.html', context)

def projects_searchbar(request):
    searchbar = request.GET.get('search')
    post = Project.objects.all().filter(Q(title__icontains=searchbar) | Q(description__icontains=searchbar))
    return render(request, 'project/search_bar.html', {'post':post,} )
    

