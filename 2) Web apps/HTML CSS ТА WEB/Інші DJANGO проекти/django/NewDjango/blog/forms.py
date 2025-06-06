from django import forms

class UserForm(forms.Form):
    agree = forms.BooleanField(
        label="Agree with terms",
        required=True,
        initial=False,
        help_text="Click here!",
    )

    name = forms.CharField(
        label="Name",
        max_length=50,
        min_length=2,
        strip=True,
        empty_value="",
        initial="Your name",
        help_text="Enter your name (2 - 50 symbols)",
        widget=forms.TextInput(attrs={"class": "input-name"})
    )

    email = forms.EmailField(
        label="Email",
        required=False,
        min_length=6,
        help_text="Enter your valid email",
        widget=forms.TextInput(attrs={"class": "input-email"})
    )

    age = forms.IntegerField(
        label="Age",
        min_value=1,
        max_value=120,
        help_text="Enter your age from 1 to 120"
    )

    website = forms.URLField(
        label="Site",
        required=False,
        help_text="Enter url (Example: https://examle.com)"
    )

    language = forms.ChoiceField(
        label="Language",
        choices=[
            ("en", "English"),
            ("uk", "Українська"),
            ("de", "Deutsch")
        ],
        initial="uk",
        help_text="Choice language"
    )

    skills = forms.MultipleChoiceField(
        label="Skills",
        choices=[
            ("python", "Python"),
            ("js", "JavaScript"),
            ("html", "HTML")
        ],
        required=False,
        help_text="Choice your skills"
    )

    resume = forms.FileField(
        label="Resume file (PDF)",
        required=False,
        help_text="Add your resume"
    )

    btn = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"type":"submit", "value":"Send"})
    )


class UserFormStyled(forms.Form):
    name = forms.CharField(
        min_length=3,
        widget=forms.TextInput(attrs={"class": "input_name"})
    )
    age = forms.IntegerField(
        min_value=1,
        max_value=100,
        widget = forms.TextInput(attrs={"class": "input_age"})
    )


