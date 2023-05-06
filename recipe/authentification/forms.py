from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class ProfileUpdateForm(forms.ModelForm):
    current_password = forms.CharField(required=False, widget=forms.PasswordInput())
    new_password1 = forms.CharField(required=False, widget=forms.PasswordInput())
    new_password2 = forms.CharField(required=False, widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['name', 'email', 'bio', 'image']

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('New passwords do not match.')
        if current_password and not self.instance.user.check_password(current_password):
            raise forms.ValidationError('Invalid current password.')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        user = instance.user
        current_password = self.cleaned_data.get('current_password')
        new_password1 = self.cleaned_data.get('new_password1')
        if current_password and new_password1:
            user.set_password(new_password1)
        instance.save()
        if commit:
            user.save()
        return instance