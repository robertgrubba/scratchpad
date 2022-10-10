from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=300, null=True, blank=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(default='a')

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Topic,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic.title + ": " +self.title

    class Meta:
        ordering = ['created']


