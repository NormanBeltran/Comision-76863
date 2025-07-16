from django.shortcuts import render

from .models import *

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
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

class MovieCreate(CreateView):
    model = Movie    
    fields = "__all__"
    success_url = reverse_lazy('home')