from django import forms
from django.contrib.auth.models import User
from .apps.trail.models import UserProfile
from django.utils.text import slugify

from .apps.trail.models import *

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')
        
class AddProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'title',
            'category',
            'description',
            'url',
        )
        category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'))

    def save(self):
        if self.instance.pk:
            return super(AddProject, self).save()
            
        instance = super(AddProject, self).save(commit=False)
        instance.slug =  slugify(instance.title)
        instance.save()

        return instance