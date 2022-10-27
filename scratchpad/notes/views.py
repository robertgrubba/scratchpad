from django.shortcuts import render
from django.urls import reverse_lazy
from django import forms
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView
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

class CategoryDeleteView(LoginRequiredMixin,DeleteView):
    model = Category
    success_url = reverse_lazy('notes:categories')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        super().delete(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('notes:categories')

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

class TopicDeleteView(LoginRequiredMixin,DeleteView):
    model = Topic
    success_url = reverse_lazy('notes:category')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        super().delete(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('notes:category', kwargs={'slug': self.object.category.slug})


class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Note
    
    fields = ['title','text']

    def form_valid(self,form):
        if Note.objects.filter(title=form.instance.title).exists():
            raise forms.ValidationError("Try not to duplicate notes titles")
        else:
            form.instance.topic = Topic.objects.filter(slug=self.request.session['lasttop']['slug'],owner=self.request.user).first()
            return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin,UpdateView):
    model = Note
    fields = ['title','text']
    template_name_suffix = '_update_form'

class NoteDeleteView(LoginRequiredMixin,DeleteView):
    model = Note
    success_url = reverse_lazy('notes:topics')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        super().delete(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('notes:topic', kwargs={'slug': self.object.topic.slug})


class AttachementCreateView(LoginRequiredMixin,CreateView):
    model = Attachement

    fields = ['file']

    def form_valid(self,form):
        form.instance.note = Note.objects.filter(id=self.kwargs['id']).first()
        return super().form_valid(form)


 
