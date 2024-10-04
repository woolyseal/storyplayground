from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from rpgs.models import RolePlay

class RolePlayForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget(), required=False)
    
    class Meta:
        model = RolePlay
        fields = ['title', 'description']