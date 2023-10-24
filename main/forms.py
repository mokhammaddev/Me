from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": "input100",
            "type": "text",
            "placeholder": "Full name",
            "name": "name"
        })
        self.fields['email'].widget.attrs.update({
            "class": "input100",
            "type": "email",
            "name": "email",
            "placeholder": "E-mail",
        })
        self.fields['phone_number'].widget.attrs.update({
            "class": "input100",
            "type": "number",
            "name": "phone",
            "placeholder": "Phone",
        })
        self.fields['message'].widget.attrs.update({
            "class": "input100",
            "name": "message",
            "placeholder": "Your Message",
        })
