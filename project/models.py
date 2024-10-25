from django.db import models
import uuid
from users.models import Profil
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True,  default='images/it.png')
    demo_link = models.CharField(max_length=400, null=True, blank=True)
    source_link = models.CharField(max_length=400, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    vote_count = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    tag = models.ManyToManyField('Tag', blank = True, related_name="proj_tag")
    
    def __str__(self) -> str:
        return self.title
    
    
class Review(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.SET_NULL, null=True, blank=True)
    VOTE_TYPE = {
        ('+', 'ijobiy'),
        ('-', 'salbiy'),
    }
    body = models.TextField(default='')
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    project = models.ForeignKey(Project, on_delete = models.CASCADE, null=True, blank =True, related_name='project_review')
    
    def __str__(self) -> str:
        return self.value
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self) -> str:
        return self.name


# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', default=1)
#     post_name = models.ForeignKey(Project, on_delete=models.CASCADE)
#     body = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f'Comment by {self.user.username} on {self.project.title}'