from django import forms
from contact.models import Contact
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):

    from_email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'input-field', 'placeholder': 'Please leave your email address here'}), label='')
    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'input-field', 'placeholder': 'Subject'}), label='')
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'input-field', 'placeholder': 'Message'}), label='')
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = [
            'from_email',
            'subject',
            'message'
        ]

    '''
    #No need this anymore. EmailField already check this out
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is None:
            raise forms.ValidationError("Invalid email")
        return email
        '''
