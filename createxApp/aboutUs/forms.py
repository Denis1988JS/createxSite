from django import forms
from .models import *

class SuscribeUserSVModelForm(forms.ModelForm):

    class Meta:
        model = SuscribeUserSVModel
        fields = ('userName','userEmail')
        labels = {'userName': 'Name*', 'userEmail': 'Email',}
        widgets = {
            'userName': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'userEmail': forms.EmailInput(attrs={'placeholder': 'Your working email', 'type': 'email'})
        }


class UserSendCVModelForm(forms.ModelForm):
    # метод наследования - устанавливаем пустое поле в поле категория
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['userLocation'].empty_label = 'Choose your location'
    class Meta:
        model = UserSendCVModel
        fields = ('userName','userLocation','userTell','userEmail','userMessage','userCVFile')
        widgets = {
             'userName': forms.TextInput(attrs={'placeholder': 'Your name'}),
             'userTell': forms.TextInput(attrs={'placeholder': 'Your phone number', "type":'tel'}),
             'userEmail': forms.EmailInput(attrs={'placeholder': 'Your working email', 'type': 'email'}),
             'userMessage': forms.Textarea(attrs={'placeholder': 'Your covering letter'}),
        }
