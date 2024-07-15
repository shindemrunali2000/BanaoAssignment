from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=6)
    user_type = forms.ChoiceField(choices=Profile.USER_TYPES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'profile_picture', 'address_line1', 'city', 'state', 'pincode', 'user_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile.objects.create(
                user=user,
                profile_picture=self.cleaned_data.get('profile_picture'),
                address_line1=self.cleaned_data.get('address_line1'),
                city=self.cleaned_data.get('city'),
                state=self.cleaned_data.get('state'),
                pincode=self.cleaned_data.get('pincode'),
                user_type=self.cleaned_data.get('user_type'),
            )
            print(f"User {user.username} created with profile {profile.user_type}")  # Debug statement
            profile.save()
        return user

