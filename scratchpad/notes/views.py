from django.shortcuts import render
from django import forms
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView
from .models import Topic,Category,Note,Attachement
from notes import views

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def index(request):
    return render(request, 'index.html')

class CategoryListView(LoginRequiredMixin,ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = Category
    fields = ['name']

    def form_valid(self, form):
        if Category.objects.filter(owner=self.request.user,name__iexact=form.instance.name).exists():
            raise forms.ValidationError('You are not allowed to duplicate categories')
        else:
            form.instance.owner = self.request.user
            return super().form_valid(form)

#    def clean(self):
#        if Category.objects.filter(user=self.user,name=form.instance.name).exists():
#            raise forms.ValidationError('You are not allowed to duplicate categories')


class CategoryDetailView(LoginRequiredMixin,DetailView):
    model = Category
    
    def get_queryset(self):
        self.request.session['lastcat']=self.kwargs
        return Category.objects.filter(owner=self.request.user)

class TopicDetailView(LoginRequiredMixin,DetailView):
    model = Topic

    def get_queryset(self):
        self.request.session['lasttop']=self.kwargs
        return Topic.objects.filter(owner=self.request.user)
    
class TopicCreateView(LoginRequiredMixin,CreateView):
    model = Topic
    
    fields = ['title','url']
#    def get_initial(self):
#        initial = super(TopicCreateView, self).get_initial()
#        initial = initial.copy()
#        last_cat_slug=self.request.session['lastcat']['slug']
#        return initial

 
    def form_valid(self,form):
        if Topic.objects.filter(owner=self.request.user, title=form.instance.title).exists():
            raise forms.ValidationError("You are not allowed to duplicate categories")
        else:
            form.instance.owner = self.request.user
            form.instance.category = Category.objects.filter(slug=self.request.session['lastcat']['slug'],owner=self.request.user).first()
            return super().form_valid(form)


class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Note
    
    fields = ['title','text']

    def form_valid(self,form):
        if Note.objects.filter(title=form.instance.title).exists():
            raise forms.ValidationError("Try not to duplicate notes titles")
        else:
            form.instance.topic = Topic.objects.filter(slug=self.request.session['lasttop']['slug'],owner=self.request.user).first()
            return super().form_valid(form)

class AttachementCreateView(LoginRequiredMixin,CreateView):
    model = Attachement

    fields = ['file']

    def form_valid(self,form):
        if Attachement.objects.filter(file=form.instance.file).exists():
            raise forms.ValidationError("Try not to duplicate attachements")
        else:
            form.instance.note = self.request.id
            return super().form_valid(form)


 
