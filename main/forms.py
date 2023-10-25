from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": "form-control",
            "id": "name",
            "type": "text",
            "placeholder": "Your Name",
            "name": "name"
        })
        self.fields['email'].widget.attrs.update({
            "class": "form-control",
            "id": "email",
            "type": "email",
            "name": "email",
            "placeholder": "Your Email",
        })
        self.fields['phone_number'].widget.attrs.update({
            "class": "form-control",
            "type": "number",
            "name": "phone",
            "placeholder": "Phone number",
        })
        self.fields['message'].widget.attrs.update({
            "class": "form-control",
            "name": "message",
            "rows": 5,
            "placeholder": "Message",
        })
