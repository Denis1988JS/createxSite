from django import forms
from .models import *

#Форма для подписки в footer - UserSubscribe
class UserSubscribeForm(forms.ModelForm):
    class Meta:
        model = UserSubscribe
        fields = ['userEmail']
        labels = {'userEmail':''}
        widgets = {
            'userEmail': forms.EmailInput(attrs={'placeholder': 'Your email address ', 'class':'subscribe'}),
        }

#Форма для вопросов - AskFromUser - ее доделать
class AskFromUserForm(forms.ModelForm):
    class Meta:
        model = AskFromUser
        fields = ['userName','phoneNumberUser','askContent']
        labels = {'userName': 'Name','phoneNumberUser':'Phone','askContent':'Message'}
        widgets = {
            'userName': forms.TextInput(attrs={'placeholder': 'Your name','class':'askInput w260'}),
            'phoneNumberUser': forms.TextInput(attrs={'placeholder': 'Your phone', 'class': 'askInput w260','type':'tel'}),
            'askContent': forms.TextInput(attrs={'placeholder': 'Your message', 'class': 'askInput w414'}),
        }

#Форма обсуждение от пользователя - DiscussForUser
class DiscussForUserForm(forms.ModelForm):
    class Meta:
        model = DiscussForUser
        fields = ['userName','phoneNumberUser','emailUser','discussContent','userAgree']
        labels = {'userName':'Name*','phoneNumberUser':'Phone*','emailUser':'Email','discussContent':'Message*','userAgree':'I agree to receive communications from Createx Construction Bureau.'}
        widgets = {
            'discussContent':forms.Textarea(attrs={'class':'messageD','placeholder':'Your message'}),
            'userName': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'phoneNumberUser': forms.TextInput(attrs={'placeholder': 'Your phone number', 'type':'tel'}),
            'emailUser': forms.EmailInput(attrs={'placeholder': 'Your working email', 'type': 'email'}),
            'userAgree': forms.CheckboxInput(attrs={'class':'iAgree'}),
        }