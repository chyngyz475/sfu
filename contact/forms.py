from django import forms

from fields import ReCaptchaField

class ReCaptchaForm(forms.Form):
    subject = forms.CharField(
            label='Your subject',
            widget=forms.TextInput(
                    attrs={'class': 'validate[required] text-input'}))
    email = forms.EmailField(
            label='Your e-mail address',
            required=False,
            widget=forms.TextInput(attrs={'class': 'validate[required,custom[email]] text-input'}))
    message = forms.CharField(
            label='Your message',
            widget=forms.Textarea(attrs={'class': 'validate[required,custom[onlyLetterNumber]] text-input'}))
    recaptcha = ReCaptchaField()