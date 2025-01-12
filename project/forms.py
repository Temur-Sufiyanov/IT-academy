from django import forms
from django.forms import ModelForm
from .views import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'demo_link', 'source_link', 'vote_count', 'vote_ratio', 'tag']
        
        widgets = {
            'tag': forms.CheckboxSelectMultiple()
        }
        
    def __init__(self, *args, **kwargs ):
        super(ModelForm, self).__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})
            
# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['body']
        
        
#     def __init__(self, *args, **kwargs):
#         super(ModelForm, self).__init__(*args, **kwargs)
        
#         for key, field in self.fields.items():
#             field.widget.attrs.update({"class": "input input--textarea"})