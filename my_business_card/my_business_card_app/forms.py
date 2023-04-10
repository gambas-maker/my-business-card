from django import forms 
from my_business_card_app.models import User, UserProfile

class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ("profile_pic")
