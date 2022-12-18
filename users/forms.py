from django import forms
from .models import User

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=256,required=True)
    bio = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = User
        fields = '__all__'

