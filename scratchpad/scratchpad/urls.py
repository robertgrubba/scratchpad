"""scratchpad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('team',views.team,name='team'),
    path('blog',views.blog,name='blog'),
    path('pricing',views.pricing,name='pricing'),
    path('contact',views.contact,name='contact'),
    path('notes', include('notes.urls')),

]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

