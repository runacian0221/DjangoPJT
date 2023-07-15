from profile import Profile
from django.forms import ModelForm


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
        