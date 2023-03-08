from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'students/home.html'

class LitDetailView(TemplateView):
    template_name = 'students/literature.html'

class TaskView(TemplateView):
    template_name = 'students/tasks.html'