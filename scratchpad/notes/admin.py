from django.contrib import admin

# Register your models here.

from .models import Category,Topic,Note,Attachement


class NoteInline(admin.StackedInline):
    model = Note
    extra = 1
    exclude = ['created']
#    readonly_fields = ['created']

class TopicAdmin(admin.ModelAdmin):
#    fieldsets = [
#        ( None, {
#            'fields':['name','description','price','amount','minimum']}),
#        ]
    inlines = [NoteInline]

admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Attachement)
admin.site.register(Topic,TopicAdmin)
#admin.site.register(Topic)
