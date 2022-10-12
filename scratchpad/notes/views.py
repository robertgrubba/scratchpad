from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Topic,Category,Note
from notes import views
# Create your views here.

def index(request):
    return render(request, 'index.html')

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

class TopicDetailView(DetailView):
    model = Topic

