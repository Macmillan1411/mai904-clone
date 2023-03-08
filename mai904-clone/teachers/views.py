from django.shortcuts import render
from .models import Teacher
from django.views.generic import ListView

# Create your views here.
class TeachersView(ListView):
    model = Teacher
    template_name = 'teachers/teachers_list.html'


