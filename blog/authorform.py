from django.forms import ModelForm
from .models import author

class authorForm(ModelForm):
    class Meta:
        model=author
        fields=['aname','address']