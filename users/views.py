from django.shortcuts import render, redirect
from .models import Profil, Skill
from project.models import Project
from django.contrib.auth import authenticate, login, logout
from .forms import CostumUserCreationForm, CostumProfilCreationForm, CostumSkillChangingForm, CostumSkillCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

def profiles(request):
    users = Profil.objects.all()
    paginator = Paginator(users, 3)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    
    
    return render(request, 'users/profiles.html', context)

def profile(request, pk):
    one_user =Profil.objects.get(id=pk)
    context = {
        'one_user':one_user,
    }
    
    return render(request, 'users/profile.html', context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Siz tizimga kirdingiz')
            return redirect('profiles')
        else:
            messages.error(request, 'Bunday foydlanuvchi mavjud emas!')
    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    messages.info(request, " Siz tizimdan chiqdingiz!")
    return redirect('profiles')


def register_user(request):
    form = CostumUserCreationForm()
    for f in form:
        if f.label == 'Password':
            f.label = 'Parol'
        if f.label == 'Password confirmation':
            f.label = 'Parolni qayta kiriting'
    context = {
        'form': form,
    }
    
    if request.method == 'POST':
        form = CostumUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, "Siz muvafaqiyatli ro'yxatdan o'dingiz")
            return redirect('profiles')
        else:
            messages.error(request, "Siz ro'yxatdan o'tmadingiz! iltimos qaytadan urinib ko'ring")
    return render(request, 'users/signup.html', context)

@login_required(login_url='/login/')
def account_user(request):
    account_user = request.user.profil
    context = {
        'account_user':account_user,
    }
    return render(request, 'users/account.html', context)

@login_required(login_url='/login/')
def account_edit(request):
    profil = request.user.profil
    form = CostumProfilCreationForm(instance=profil)
    if request.method == 'POST':
        form = CostumProfilCreationForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil muvafaqiyatli o'zgartirildi")
            return redirect('account')
    context = {
        'form':form,
    }
    return render(request, 'users/account_edit.html', context)

@login_required(login_url='/login/')
def account_skill_change(request,id):
    profil_skills = Skill.objects.get(id=id)
    form = CostumSkillChangingForm(instance=profil_skills)
    
    if request.method == 'POST':
        form = CostumSkillChangingForm(request.POST, request.FILES, instance=profil_skills)
        if form.is_valid():
            form.save()
            messages.success(request, "Malakalar muvafaqiyatli o'zgartirildi")
            return redirect('account')
    context = {
        'form':form,
    }
    
    return render(request, 'users/account_skill_change.html', context)

@login_required(login_url='/login/')
def account_skill_delete(request, id):
    profil_skills_delete = Skill.objects.get(id=id)
    if request.method == "POST":
        profil_skills_delete.delete()
        messages.success(request, "Malakalar muvafaqiyatli o'chirildi")
        return redirect('account')
    context = {
        'profil_skills_delete':profil_skills_delete,
    }
    
    return render(request, 'users/account_skill_delete.html',context)


@login_required(login_url='/login/')
def account_skill_add(request):
    if request.method == 'POST':
        skill = CostumSkillCreationForm(request.POST, request.FILES)
        if skill.is_valid():
            skills = skill.save(commit=False)
            skills.user = request.user.profil
            skills.save()
            messages.success(request, "Malakalar muvafaqiyatli qo'shildi")
            return redirect('account')
    else:
        skill = CostumSkillCreationForm() 
    context = {
        'skill': skill,
    }
    return render(request, 'users/account_skill_creating.html', context)


def account_searchbar(request):
    if request.method == "GET":
        search_bar = request.GET.get('search')
        profil = Profil.objects.all().filter(name=search_bar)
        return render(request, 'users/search_bar.html', {'profil':profil,})