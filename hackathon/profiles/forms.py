"""
Hackathon #hackRussia
"""

from django import forms
from django.contrib.auth.models import User


class EditForm(forms.ModelForm):
    """
    For default Django user model
    """

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class SignupForm(forms.Form):
    username = forms.RegexField(
        regex=r"^[a-zA-Z0-9\-_]+$",
        widget=forms.TextInput(
            attrs={
                "required": True,
                "max_length": 32
            }
        ),
        error_messages={
            "invalid": "Имя пользователя может состоять только из символов "
                       "латинского алфавита, цифр, тире и нижнего "
                       "подчеркивания, и не привышать длину в 32 символа."
        }
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "required": True,
                "max_length": 64
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "required": True,
                "max_length": 64,
                "render_value": False
            }
        )
    )

    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "required": True,
                "max_length": 64,
                "render_value": False
            }
        ),
        label="Password (again)"
    )

    first_name = forms.RegexField(
        regex=r"^\w+$",
        widget=forms.TextInput(
            attrs={
                "required": True,
                "max_length": 64
            }
        )
    )

    last_name = forms.RegexField(
        regex=r"^\w+$",
        widget=forms.TextInput(
            attrs={
                "required": True,
                "max_length": 64
            }
        )
    )

    def clean_username(self):
        try:
            User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(
            "Пользователь с таким username уже существует.")

    def clean_email(self):
        try:
            User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError("Данный Email уже занят.")

    def clean(self):
        if 'password' in self.cleaned_data \
                and 'password_confirmation' in self.cleaned_data:
            if self.cleaned_data['password'] \
                    != self.cleaned_data['password_confirmation']:
                raise forms.ValidationError("Пароли не совпадают!.")
        return self.cleaned_data
