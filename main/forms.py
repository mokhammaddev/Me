from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": "fname",
            "type": "text",
            "placeholder": "Full name",
            "name": "name"
        })
        self.fields['email'].widget.attrs.update({
            "type": "email",
            "placeholder": "Email",
        })
        self.fields['phone_number'].widget.attrs.update({
            "type": "number",
            "placeholder": "Phone number",
        })
        self.fields['message'].widget.attrs.update({
            # "class": "form-control",
            "placeholder": "Message",
        })
