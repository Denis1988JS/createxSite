from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView,View
from  django.contrib import messages
from contacts.forms import ContactsForm
from createx.models import HeaderContent
from createx.utils import FormsMixin
# Create your views here.


class ContactsView(FormsMixin,TemplateView):
    template_name = 'contacts/contacts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Страница контакты'
        context['header'] = HeaderContent.objects.get(title='CONTACTS')
        context['form'] = ContactsForm
        c_def = self.get_user_context()
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class AddContact(View):
    def post(self, request):
        form = ContactsForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form = form.save()
            messages.success(request, 'Сообщение отправлено !!!')
            return redirect('contacts')
        else:
            print(request.POST)
            print(form.errors)

            messages.success(request, 'Сообщение не отправлено')
            return redirect('contacts')

