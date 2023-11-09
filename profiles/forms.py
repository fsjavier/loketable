from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """
    Form to edit a profile
    """

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'bio',
            'image',
            'country',
            'city',
            'contact'
        ]

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'bio': 'Bio',
            'image': 'Profile Picture',
            'country': 'Country',
            'city': 'City',
            'contact': 'Contact Information'
        }
