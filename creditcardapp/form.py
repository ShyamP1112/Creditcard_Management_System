from django import forms
from .models import usersignup, creditcardapply,contacts


class usersignupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'

class creditcardapplyForm(forms.ModelForm):
    class Meta:
        model=creditcardapply
        fields='__all__'

class contactsForm(forms.ModelForm):
    class Meta:
        model=contacts
        fields='__all__'