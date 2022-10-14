from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from notes import views
#from ingredient.views import IngredientListView

app_name='notes'

urlpatterns = [
        path('', views.CategoryListView.as_view(), name='categories'),
        path('/category/create', views.CategoryCreateView.as_view(), name='category_create'),
        path('/category/<slug:slug>', views.CategoryDetailView.as_view(), name='category'),
        path('/topic/new', views.TopicCreateView.as_view(), name='topic_create'),
        path('/topic/<slug:slug>', views.TopicDetailView.as_view(), name='topic'),
        ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


