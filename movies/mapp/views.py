from django.shortcuts import render

from .models import *
from .forms import *

from django.contrib.auth.views import LoginView

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = 'mapp/index.html'

class GenderList(ListView):
    model = Gender

    #def get_queryset(self):
    #    return Gender.objects.filter(name__icontains="i").order_by('id').values()

class CompanyList(ListView):
    model = Company

class MovieList(ListView):
    model = Movie    

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie    
    form_class = MovieForm
    success_url = reverse_lazy('home')

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie    
    form_class = MovieForm
    success_url = reverse_lazy('home')    

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie    
    success_url = reverse_lazy('home')   

class MyLoginView(LoginView):
    redirect_authenticated_user = True