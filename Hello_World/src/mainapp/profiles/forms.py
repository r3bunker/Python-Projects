from django.forms import ModelForm
from .models import Profiles


class ProfileForm(ModelForm):
    class Meta:
        model = Profiles
        fields = '__all__'
