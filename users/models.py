from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import Signal, receiver
# Create your models here.

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    info = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    bio= models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='profils/', default='profils/default_profile.webp')
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_instagram = models.CharField(max_length=50, null=True, blank=True)
    social_tegramm = models.CharField(max_length=50, null=True, blank=True)
    tag_skills = models.ManyToManyField('Skill', blank=True, related_name='prof_skill')
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return str(self.user.username)
    
    
    
    
    
class Skill(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return str(self.name)
  
  
  
