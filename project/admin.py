from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Review)
# admin.site.register(Comment)