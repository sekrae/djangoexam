from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserForm
from .models import User


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    fields = ('username', 'password')
    success_url = reverse_lazy('worker_list')