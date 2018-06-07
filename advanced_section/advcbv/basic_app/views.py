from django.shortcuts import render
from django.views.generic import View, TemplateView,ListView,DetailView
from . import models

class SchoolListView(ListView):
    context_object_name = 'school_listy'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detaily'
    model = models.School
    template_name = 'basic_app/school_detail.html'


