from django import forms
from django.forms import ModelForm
from .models import Admin
class adminform(ModelForm):
    class Meta:
        model =Admin
        fields = ('admin_id','admin_name','password')
    