from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Topic,Category,Note
from notes import views

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def index(request):
    return render(request, 'index.html')

class CategoryListView(LoginRequiredMixin,ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

class CategoryDetailView(LoginRequiredMixin,DetailView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

class TopicDetailView(LoginRequiredMixin,DetailView):
    model = Topic

