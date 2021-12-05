from django.shortcuts import render
from django.http import request
from django.views import generic
from blog import models

class Index(generic.ListView):
    model = models.Post
    template_name = 'index.html'

class Post(generic.DetailView):
    model = models.Post
    template_name = 'post.html'

class About(generic.TemplateView):
    template_name = 'about.html'