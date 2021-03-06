from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from utils.upload import handle_uploaded_file
from users.models import Profile

AuthUserModel = get_user_model()


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=128,required=True, label='First name')
    last_name = forms.CharField(max_length=128, required=True, label='Last name')
    username = forms.CharField(max_length=128, required=True, label='Username')
    email = forms.CharField(max_length=128, required=True, label='Email')
    password = forms.CharField(max_length=128, required=True, label='Password', widget=forms.PasswordInput)
    password_confirmation = forms.CharField(max_length=128, required=True, label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            AuthUserModel.objects.get(username=username)
        except AuthUserModel.DoesNotExist:
            return username

        raise forms.ValidationError(f'{username} already exist')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            AuthUserModel.objects.get(email=email)
        except AuthUserModel.DoesNotExist:
            return email

        raise forms.ValidationError(f'{email} already exist')

    def clean_password(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')

        user = AuthUserModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        validate_password(password, user=user)
        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation=self.cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError('Password not confirmed')

        return password_confirmation

    def save(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')

        user = AuthUserModel(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', ]

