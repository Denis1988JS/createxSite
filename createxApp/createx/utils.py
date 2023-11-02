from .forms import DiscussForUserForm,UserSubscribeForm,AskFromUserForm

class FormsMixin:
    def get_user_context(self,**kwargs):
        context = kwargs
        context['AskFromUserForm'] = AskFromUserForm
        context['UserSubscribeForm'] = UserSubscribeForm
        context['DiscussForUserForm'] = DiscussForUserForm
        return context
