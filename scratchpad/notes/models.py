from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.owner.username +": "+self.name

    def get_absolute_url(self):
        return reverse('notes:categories')

class Topic(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=300, null=True, blank=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='topics')
    slug = models.SlugField(default='a')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='topic')

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Topic,self).save(*args, **kwargs)

    def __str__(self):
        return self.owner.username +": "+self.title

    def get_absolute_url(self):
        return reverse('notes:topic', args=[str(self.slug)])

    class Meta:
        ordering = ['title']

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,related_name='notes')

    def __str__(self):
        return self.topic.title + ": " +self.title

    def get_absolute_url(self):
        return reverse('notes:topic', args=[str(self.topic.slug)])

    class Meta:
        ordering = ['created']


class Attachement(models.Model):
    file = models.FileField(upload_to='uploads/%Y/%m/%d/',null=True,blank=True,default=None)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True, related_name='attachements')

    def get_extension(self):
        filename = self.file.name
        return str(filename.split('.')[-1])

    def __str__(self):
        return str(self.file.name)

    def get_absolute_url(self):
        return reverse('notes:topic', args=[str(self.note.topic.slug)])
