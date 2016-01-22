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

class AddSpark(forms.ModelForm):
    class Meta:
        model = Spark
        fields = (
            'name',
            'category',
            'start_date',
            'end_date',
            'url',
            'description',
        )
        category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'))
        widgets = {
            'start_date' : forms.DateInput(attrs={'type':'date'}),
            'end_date' : forms.DateInput(attrs={'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author')
        super().__init__(*args, **kwargs)


    def save(self):
        if self.instance.pk:
            return super(AddSpark, self).save()
        instance = super(AddSpark, self).save(commit=False)
        instance.slug =  slugify(instance.name)
        instance.author = self.author
        instance.save()

        return instance
