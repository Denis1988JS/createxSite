from django import forms

from .models import NewsCommentsModefl, NewsModel

class NewsCommentsModeflForm(forms.ModelForm):
    class Meta:
        model = NewsCommentsModefl
        fields = ['user_name','user_email','comment']
        labels = {'user_name': 'Name*', 'user_email': 'Email*', 'comment': 'Your comment*'}
        widgets = {
            "user_name": forms.TextInput(attrs={'placeholder': 'Your name','class':'name_comment'}),
            "user_email": forms.EmailInput(attrs={'placeholder': 'Your working email','class':'email_comment'}),
            "comment": forms.Textarea(attrs={'placeholder': 'Type comment here','class':'comment'})
        }
