from django import forms
from .models import News

class UpdateNewsForm(forms.ModelForm):
    title = forms.CharField()
    details = forms.Textarea
    

    class Meta:
        model = News
        fields = ['title' , 'details']