from aboutUs.models import OurSocLinks
from .forms import DiscussForUserForm,UserSubscribeForm,AskFromUserForm

class FormsMixin:
    def get_user_context(self,**kwargs):
        context = kwargs
        context['social_links'] = OurSocLinks.objects.all()
        context['AskFromUserForm'] = AskFromUserForm
        context['UserSubscribeForm'] = UserSubscribeForm
        context['DiscussForUserForm'] = DiscussForUserForm
        return context
