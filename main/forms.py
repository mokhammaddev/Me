from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = '__all__'
        fields = ('name', 'email', 'phone_number', 'subject', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": "form-control",
            "id": "name",
            "type": "text",
            "name": "name",
        })
        self.fields['email'].widget.attrs.update({
            "class": "form-control",
            "id": "email",
            "type": "email",
            "name": "email",
        })
        self.fields['phone_number'].widget.attrs.update({
            "class": "form-control",
            "type": "number",
            "name": "subject",
            "id": "subject",
        })
        self.fields['subject'].widget.attrs.update({
            "class": "form-control",
            "type": "text",
            "name": "subject",
            "id": "subject",
        })
        self.fields['message'].widget.attrs.update({
            "class": "form-control",
            "name": "message",
            "rows": 10,
        })
