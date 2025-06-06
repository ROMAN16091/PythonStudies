from django import forms
from .models import Book
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'genre']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        classes = {
            'username': 'input-username',
            'email': 'input-email',
            'password1': 'pw1',
            'password2': 'pw2'
        }
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        for name, field in self.fields.items():
            css_class = classes.get(name, 'form-control')
            field.widget.attrs.update({
                'class': css_class,
                'placeholder': field.label
            })
