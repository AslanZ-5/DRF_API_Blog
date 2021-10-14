from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm,
                                       PasswordChangeForm
                                       )
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileform
from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordChangingForm
from django.views.generic import DetailView
from myblog.models import Profile


class EditProfilePageView(generic.UpdateView):
    model = Profile
    success_url = reverse_lazy('home')
    template_name = 'registration/edit_profile_page.html'
    fields = ['image', 'biograph', 'fb_url', 'tw_url', 'inst_url']


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')
    template_name = 'registration/change_password.html'


def password_success(request):
    return render(request, 'registration/password_success.html')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileform
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
