from django import forms
from .models import *

contact_method = [
    ("Phone", "Phone"),
    ("Email", "Email"),
    ("Viber", "Viber"),
    ("Whatsapp", "Whatsapp"),
]

class ContactsForm(forms.ModelForm):
    contact = forms.CharField(widget=forms.RadioSelect(choices=contact_method))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['interesting'].empty_label =  None
        self.fields['contact'].empty_label = None
        self.fields['location'].empty_label = None
    class Meta:
        model = Contacts
        fields = ('name', 'interesting','phoneNumberUser','location','userEmail','contact','userMessage','userAgree')
        labels = {'name': 'Name*', 'interesting': 'I am interested in','phoneNumberUser':'Phone*','location':'location*','userEmail':'Email',
                  'contact':'Preferred contact method','userMessage':'Message*','userAgree':'I agree to receive communications from Createx Construction Bureau.'}
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Your name'}),
            'userEmail': forms.EmailInput(attrs={'placeholder': 'Your working email', 'type': 'email'}),
            'phoneNumberUser': forms.TextInput(attrs={'placeholder': 'Your phone number', "type":'tel'}),
           # 'contact': forms.RadioSelect(attrs={"required":False,}),
            'userMessage': forms.Textarea(attrs={'placeholder': 'Your  message'}),
            'userAgree': forms.CheckboxInput(attrs={'class': 'iAgree'}),

        }