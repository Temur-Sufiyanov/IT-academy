from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Profil, Skill

class CostumUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Ism', 
            'last_name': 'Sharif', 
            'email': 'Elektron manzil',
            'username': 'Login',
        }
        
    def __init__(self, *args, **kwargs ):
        super(ModelForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})   
            

class CostumProfilCreationForm(ModelForm):
    class Meta:
        model = Profil
        fields = ['name','email','info','location','bio','image','social_github','social_instagram','social_tegramm','tag_skills']
        labels = {
            'tag_skills':'Skills',
        }

        widgets = {
            'tag_skills': forms.CheckboxSelectMultiple()
        }
        
    
    
    def __init__(self, *args, **kwargs ):
        super(ModelForm, self).__init__(*args, **kwargs)
    
        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})   
        
class CostumSkillChangingForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']
        
        
    def __init__(self, *args, **kwargs ):
        super(ModelForm, self).__init__(*args, **kwargs)
    
        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})   
     
            
class CostumSkillCreationForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']
        
        
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})
         
        