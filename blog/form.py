from django.forms import ModelForm
from .models import blog,author

class blogForm(ModelForm):
    class Meta:
        model=blog
        fields=['title','description','conauthor']