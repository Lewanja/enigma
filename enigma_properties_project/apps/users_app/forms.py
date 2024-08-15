from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widget = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username':('only 150 characters or less required. Can be Letters, digits and @/./+/-/_ only'),
            'password1':("Your password can’t be too similar to your other personal information,"
                          " at least 8 characters.Your password can’t be a commonly used password, "
                          "can’t be entirely numeric."),
            'password2':('Enter the same password as before, for verification.'),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.help_text:
                field.help_text = f'<small class="form-text text-muted">{field.help_text}</small>'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
