from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile
from .forms import ProfileForm


class Profiles(generic.DetailView):
    """ View User Profile """
    template_name = 'profiles/profile.html'
    model = Profile
    context_object_name = 'profile'


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """ Edit a Profile """
    template_name = 'profiles/edit_profile.html'
    form_class = ProfileForm
    model = Profile

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.user.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EditProfile, self).form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user
